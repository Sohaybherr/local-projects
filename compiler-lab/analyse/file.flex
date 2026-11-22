
import java.io.IOException;
import java.io.InputStream;

/* ---------- Partie 2 : options JFlex ---------- */
%%
%public
%class EBNFScanner
%implements EBNFTokens
%unicode
%integer
%function nextToken

%{

// القيمة ديال IDENT و LITERAL
public String chrs = "";

%}

/* ---------- Partie 3 : définitions (macros) ---------- */

LETTER   = [A-Za-z]
DIGIT    = [0-9]
IDENT    = {LETTER}({LETTER}|{DIGIT}|_)*

STRING   = \"([^\"\\\n\r]|\\.)*\"   // chaîne entre " "

/* ---------- Partie 4 : règles ---------- */
%%

/* Identificateurs */
{IDENT}        {
                  chrs = yytext();
                  return IDENT;
               }

/* LITTERAL entre " " */
{STRING}       {
                  String s = yytext();
                  chrs = s.substring(1, s.length() - 1); // حذف "
                  return LITERAL;
               }

/* Symboles */
"("            { return LPAREN; }
")"            { return RPAREN; }
"{"            { return LBRACE; }
"}"            { return RBRACE; }
"["            { return LBRACK; }
"]"            { return RBRACK; }
"|"            { return BAR;    }
"="            { return EQL;    }
"."            { return PERIOD; }

/* Espaces blancs */
[ \t\r\n]+     { /* skip */ }

/* Caractère inconnu */
.              {
                  System.err.println("Caractère inconnu : " + yytext());
                  return BAD;
               }

/* Fin de fichier */
<<EOF>>        { return EOF; }
