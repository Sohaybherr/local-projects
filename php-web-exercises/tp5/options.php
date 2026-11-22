<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    setcookie("textColor", $_POST["textColor"], time() + 864000, "/");
    setcookie("bgColor", $_POST["bgColor"], time() + 864000, "/");
    setcookie("lang", $_POST["lang"], time() + 864000, "/");

    header("Location: options.php");
    exit();
}

include("header.php");
?>

<h3>Options</h3>

<form method="POST" action="">
    <label>Couleur du texte :</label>
    <input type="color" name="textColor" value="<?php echo getTextColor(); ?>">

    <label>Couleur de l'arrière-plan :</label>
    <input type="color" name="bgColor" value="<?php echo getBgColor(); ?>">

    <label>Langue :</label>
    <select name="lang">
        <option value="FR" <?php if (getLang() == "FR") echo "selected"; ?>>Français</option>
        <option value="EN" <?php if (getLang() == "EN") echo "selected"; ?>>English</option>
    </select>

    <input type="submit" value="Enregistrer">
</form>

<?php include("footer.php"); ?>