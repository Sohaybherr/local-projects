<?php
session_start();
require_once("fonctions.php");

$textColor = getTextColor();
$bgColor = getBgColor();
$lang = getLang();
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Gestion des étudiants</title>
    <style>
        body{
            font-family: Arial, sans-serif;
            width: 900px;
            margin: 20px auto;
            color: <?php echo $textColor; ?>;
            background: <?php echo $bgColor; ?>;
        }
        .top{
            display:flex;
            justify-content:space-between;
            align-items:center;
        }
        h1{ margin:0; }
        table{
            width:100%;
            border-collapse:collapse;
            margin-top:15px;
        }
        th, td{
            border:1px solid #999;
            padding:8px;
            text-align:center;
        }
        a{
            text-decoration:none;
            margin-right:15px;
        }
        .menu{
            margin-top:15px;
            margin-bottom:20px;
        }
        input, select{
            width:100%;
            padding:8px;
            margin-top:5px;
            margin-bottom:12px;
        }
        input[type="submit"]{
            width:auto;
            cursor:pointer;
        }
    </style>
</head>
<body>

<div class="top">
    <h1>TP PHP</h1>
    <div><?php afficherDate($lang); ?></div>
</div>

<h2>Faculté des Sciences Dhar Mahraz</h2>

<div class="menu">
    <a href="ListeFilieres.php">Accueil</a>
    <a href="options.php">Options</a>

    <?php if (isset($_SESSION["login"])) { ?>
        <span>Bienvenue : <?php echo $_SESSION["login"]; ?></span>
        <a href="logout.php">Déconnexion</a>
    <?php } else { ?>
        <a href="login.php">Connexion</a>
    <?php } ?>
</div>

