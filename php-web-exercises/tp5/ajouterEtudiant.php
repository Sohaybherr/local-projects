<?php
include("auth.php");
include("header.php");
include("data.php");
?>

<h3>Ajouter un nouvel étudiant</h3>

<form action="TraitementAjout.php" method="POST">
    <label>Code étudiant :</label>
    <input type="text" name="CodeEtudiant" required>

    <label>Nom :</label>
    <input type="text" name="Nom" required>

    <label>Prénom :</label>
    <input type="text" name="Prenom" required>

    <label>CIN :</label>
    <input type="text" name="CIN" required>

    <label>Adresse :</label>
    <input type="text" name="Adresse" required>

    <label>Date de naissance :</label>
    <input type="date" name="DateNaissance" required>

    <label>Filière :</label>
    <select name="Filiere" required>
        <?php foreach ($filieres as $filiere) { ?>
            <option value="<?php echo $filiere["CodeFiliere"]; ?>">
                <?php echo $filiere["IntituleFiliere"]; ?>
            </option>
        <?php } ?>
    </select>

    <label>Note :</label>
    <input type="number" name="Note" min="0" max="20" step="0.01" required>

    <input type="submit" value="Ajouter">
</form>

<?php include("footer.php"); ?>