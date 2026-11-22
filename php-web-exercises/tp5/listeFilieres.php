<?php
include("auth.php");
include("header.php");
include("data.php");
?>

<h3>Liste des filières</h3>

<table>
    <tr>
        <th>Code Filière</th>
        <th>Intitulé Filière</th>
    </tr>

    <?php foreach ($filieres as $filiere) { ?>
        <tr>
            <td><?php echo $filiere["CodeFiliere"]; ?></td>
            <td>
                <a href="ListeEtudiants.php?code=<?php echo $filiere["CodeFiliere"]; ?>">
                    <?php echo $filiere["IntituleFiliere"]; ?>
                </a>
            </td>
        </tr>
    <?php } ?>
</table>

<?php include("footer.php"); ?>