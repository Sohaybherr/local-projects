package Facu;

public class main {
  public static void main(String[] args) {
      HachList hl = new HachList();
      Etudiant e1 = new Etudiant("Alice","alice@gmail.com");
      Etudiant e2 = new Etudiant("Bob","bob@gmail.com");
      hl.addEtudiant(e1);
      hl.addEtudiant(e2);
      hl.linkEtudiantNum(e1.getId(), "123456789");
      hl.showall();
  }  
}
