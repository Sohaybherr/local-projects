// ===================== DATA =====================

// تحميل البيانات من localStorage
let etudiants = JSON.parse(localStorage.getItem("etudiants"));

if (!etudiants || etudiants.length === 0) {
  etudiants = [
    { nom: "Moujtahid", prenom: "Moujidd", note: 18 },
    { nom: "Omari", prenom: "Omar", note: 16 },
    { nom: "Kaddouri", prenom: "Kaddour", note: 15 },
    { nom: "Karimi", prenom: "Karima", note: 16 },
    { nom: "Kaslani", prenom: "Kassoul", note: 3 }
  ];
  localStorage.setItem("etudiants", JSON.stringify(etudiants));
}

// حفظ البيانات
function saveData() {
  localStorage.setItem("etudiants", JSON.stringify(etudiants));
}

// حساب mention
function mention(note) {
  if (note < 10) return "Ajourné!";
  if (note < 12) return "PASSABLE";
  if (note < 14) return "ASSEZ BIEN";
  if (note < 16) return "BIEN";
  return "TRES BIEN";
}

// ===================== LISTE =====================

if (document.getElementById("studentsTable")) {

  let table = document.getElementById("studentsTable");

  for (let i = 0; i < etudiants.length; i++) {

    let e = etudiants[i];

    table.innerHTML += `
      <tr>
        <td>${e.nom}</td>
        <td>${e.prenom}</td>
        <td>${e.note}</td>
        <td>${mention(e.note)}</td>
      </tr>
    `;
  }
}

// ===================== ADD =====================

if (document.getElementById("addForm")) {

  document.getElementById("addForm").addEventListener("submit", function(e){

    e.preventDefault();

    let nom = document.getElementById("nom").value.trim();
    let prenom = document.getElementById("prenom").value.trim();
    let note = parseFloat(document.getElementById("note").value);

    if (nom === "" || prenom === "" || isNaN(note)) {
      alert("Tous les champs sont obligatoires !");
      return;
    }

    if (note < 0 || note > 20) {
      alert("La note doit être entre 0 et 20 !");
      return;
    }

    etudiants.push({ nom, prenom, note });

    saveData();

    alert("Étudiant ajouté !");
    window.location.href = "liste.html";
  });
}

// ===================== SEARCH =====================

if (document.getElementById("search")) {

  document.getElementById("search").addEventListener("input", function(){

    let value = this.value.toLowerCase();
    let results = document.getElementById("results");

    if (value.trim() === "") {
      results.innerHTML = "";
      return;
    }

    let filtered = etudiants.filter(e =>
      e.nom.toLowerCase().includes(value) ||
      e.prenom.toLowerCase().includes(value)
    );

    if (filtered.length === 0) {
      results.innerHTML = "<p>Aucun étudiant trouvé.</p>";
      return;
    }

    let html = `
      <table>
        <tr>
          <th>Nom</th>
          <th>Prénom</th>
          <th>Note</th>
          <th>Mention</th>
        </tr>
    `;

    for (let i = 0; i < filtered.length; i++) {

      html += `
        <tr>
          <td>${filtered[i].nom}</td>
          <td>${filtered[i].prenom}</td>
          <td>${filtered[i].note}</td>
          <td>${mention(filtered[i].note)}</td>
        </tr>
      `;
    }

    html += "</table>";

    results.innerHTML = html;
  });
}

// ===================== DELETE =====================

if (document.getElementById("deleteForm")) {

  document.getElementById("deleteForm").addEventListener("submit", function(e){

    e.preventDefault();

    let value = document.getElementById("deleteInput").value.toLowerCase();

    if (value.trim() === "") {
      alert("Entrez un nom ou prénom !");
      return;
    }

    let before = etudiants.length;

    etudiants = etudiants.filter(e =>
      !(e.nom.toLowerCase().includes(value) ||
        e.prenom.toLowerCase().includes(value))
    );

    if (etudiants.length === before) {
      alert("Aucun étudiant trouvé !");
      return;
    }

    saveData();

    alert("Étudiant supprimé !");
    window.location.href = "liste.html";
  });
}