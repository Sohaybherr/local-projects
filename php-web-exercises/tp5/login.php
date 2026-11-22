<?php
session_start();
include("header.php");

$erreur = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $login = isset($_POST["login"]) ? $_POST["login"] : "";
    $password = isset($_POST["password"]) ? $_POST["password"] : "";

    if ($login == "admin" && $password == "1234") {
        $_SESSION["login"] = $login;
        header("Location: ListeFilieres.php");
        exit();
    } else {
        $erreur = "Login ou mot de passe invalide";
    }
}
?>

<h3>Authentification</h3>

<?php if ($erreur != "") { ?>
    <p style="color:red;"><?php echo $erreur; ?></p>
<?php } ?>

<form method="POST" action="">
    <label>Login :</label>
    <input type="text" name="login" required>

    <label>Mot de passe :</label>
    <input type="password" name="password" required>

    <input type="submit" value="Se connecter">
</form>

<?php include("footer.php"); ?>