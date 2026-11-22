<?php include("header.php"); ?>

<?php
$filieres = [
    ["CodeFiliere" => "GI",  "IntituleFiliere" => "Génie Informatique"],
    ["CodeFiliere" => "SMI", "IntituleFiliere" => "Sciences Mathématiques et Informatique"],
    ["CodeFiliere" => "SMA", "IntituleFiliere" => "Sciences Mathématiques Appliquées"],
    ["CodeFiliere" => "SMP", "IntituleFiliere" => "Sciences de la Matière Physique"],
    ["CodeFiliere" => "SVI", "IntituleFiliere" => "Sciences de la Vie"]
];
?>

<h2>Liste des filières</h2>

<table border="1" cellpadding="8" cellspacing="0">
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