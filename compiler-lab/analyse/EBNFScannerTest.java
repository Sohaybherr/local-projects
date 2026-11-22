import java.io.FileReader;

public class EBNFScannerTest implements EBNFTokens {

    private static String repr(int token, String chrs) {
        switch (token) {
            case BAD:     return "<bad>";
            case EOF:     return "<eof>";
            case IDENT:   return "IDENT(" + chrs + ")";
            case LITERAL: return "LITERAL(" + chrs + ")";
            case LPAREN:  return "LPAREN";
            case RPAREN:  return "RPAREN";
            case LBRACK:  return "LBRACK";
            case RBRACK:  return "RBRACK";
            case LBRACE:  return "LBRACE";
            case RBRACE:  return "RBRACE";
            case BAR:     return "BAR";
            case EQL:     return "EQL";
            case PERIOD:  return "PERIOD";
            default:      return "<?>"; 
        }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1) {
            System.err.println("Usage: java EBNFScannerTest <fichier>");
            System.exit(1);
        }

        // JFlex EBNFScanner كياخذ Reader
        EBNFScanner scan = new EBNFScanner(new FileReader(args[0]));

        int tok;
        while ((tok = scan.nextToken()) != EOF) {
            System.out.print(repr(tok, scan.chrs) + " ");
        }
        System.out.println(repr(EOF, ""));
    }

 {
    
}
}
