<?php
include("data.php");
$filieres = getListeFilieres();
$filiereChoisie = isset($_GET["filiere"]) ? $_GET["filiere"] : "";
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ajout Etudiant</title>
</head>
<body>
    <h2>Ajouter un étudiant</h2>

    <form action="insert.php" method="POST">
        <label>Code :</label><br>
        <input type="text" name="CodeE" required><br><br>

        <label>Nom :</label><br>
        <input type="text" name="Nom" required><br><br>

        <label>Prénom :</label><br>
        <input type="text" name="Prenom" required><br><br>

        <label>Filière :</label><br>
        <select name="Filiere" required>
            <?php foreach ($filieres as $f) { ?>
                <option value="<?php echo $f["CodeF"]; ?>" <?php if ($f["CodeF"] == $filiereChoisie) echo "selected"; ?>>
                    <?php echo $f["IntituleF"]; ?>
                </option>
            <?php } ?>
        </select><br><br>

        <label>Note :</label><br>
        <input type="number" name="Note" step="0.01" min="0" max="20" required><br><br>

        <input type="submit" value="Ajouter">
    </form>
</body>
</html>