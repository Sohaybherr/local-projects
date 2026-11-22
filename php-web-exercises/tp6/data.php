<?php

function ouvrirConnexion()
{
    $serveur = "localhost";
    $dbname = "SMI2020";
    $user = "root";
    $pass = "";

    try {
        $cnx = new PDO("mysql:host=$serveur;dbname=$dbname;charset=utf8", $user, $pass);
        $cnx->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $cnx;
    } catch (PDOException $e) {
        die("Erreur de connexion : " . $e->getMessage());
    }
}

function getListeFilieres()
{
    $cnx = ouvrirConnexion();
    $sql = "SELECT * FROM Filiere";
    $res = $cnx->query($sql);
    return $res->fetchAll(PDO::FETCH_ASSOC);
}

function getListeEtudiants($filiere)
{
    $cnx = ouvrirConnexion();

    $sql = "SELECT * FROM Etudiant WHERE Filiere = ? AND Note >= 10";
    $stmt = $cnx->prepare($sql);
    $stmt->execute([$filiere]);

    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

function getDetailEtudiant($code)
{
    $cnx = ouvrirConnexion();

    $sql = "SELECT * FROM Etudiant WHERE CodeE = ?";
    $stmt = $cnx->prepare($sql);
    $stmt->execute([$code]);

    return $stmt->fetch(PDO::FETCH_ASSOC);
}

function AjouterEtudiant($t)
{
    $cnx = ouvrirConnexion();

    $sql = "INSERT INTO Etudiant(CodeE, Nom, Prenom, Filiere, Note) VALUES (?, ?, ?, ?, ?)";
    $stmt = $cnx->prepare($sql);

    return $stmt->execute([
        $t["CodeE"],
        $t["Nom"],
        $t["Prenom"],
        $t["Filiere"],
        $t["Note"]
    ]);
}

function SupprimerEtudiant($c)
{
    $cnx = ouvrirConnexion();

    $sql = "DELETE FROM Etudiant WHERE CodeE = ?";
    $stmt = $cnx->prepare($sql);

    return $stmt->execute([$c]);
}

function ModifierEtudiant($t)
{
    $cnx = ouvrirConnexion();

    $sql = "UPDATE Etudiant
            SET Nom = ?, Prenom = ?, Filiere = ?, Note = ?
            WHERE CodeE = ?";
    $stmt = $cnx->prepare($sql);

    return $stmt->execute([
        $t["Nom"],
        $t["Prenom"],
        $t["Filiere"],
        $t["Note"],
        $t["CodeE"]
    ]);
}

function getIntituleFiliere($code)
{
    $cnx = ouvrirConnexion();

    $sql = "SELECT IntituleF FROM Filiere WHERE CodeF = ?";
    $stmt = $cnx->prepare($sql);
    $stmt->execute([$code]);

    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    return $row ? $row["IntituleF"] : "";
}
?>