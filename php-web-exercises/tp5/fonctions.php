<?php
function getLang()
{
    return isset($_COOKIE["lang"]) ? $_COOKIE["lang"] : "FR";
}

function getTextColor()
{
    return isset($_COOKIE["textColor"]) ? $_COOKIE["textColor"] : "#000000";
}

function getBgColor()
{
    return isset($_COOKIE["bgColor"]) ? $_COOKIE["bgColor"] : "#ffffff";
}

function afficherDate($lang = "FR")
{
    $joursFR = [
        "Sunday" => "Dimanche",
        "Monday" => "Lundi",
        "Tuesday" => "Mardi",
        "Wednesday" => "Mercredi",
        "Thursday" => "Jeudi",
        "Friday" => "Vendredi",
        "Saturday" => "Samedi"
    ];

    $moisFR = [
        "January" => "Janvier",
        "February" => "Février",
        "March" => "Mars",
        "April" => "Avril",
        "May" => "Mai",
        "June" => "Juin",
        "July" => "Juillet",
        "August" => "Août",
        "September" => "Septembre",
        "October" => "Octobre",
        "November" => "Novembre",
        "December" => "Décembre"
    ];

    

    $jourAng = date("l");
    $moisAng = date("F");
    $jourNum = date("d");
    $annee = date("Y");

    if ($lang == "FR") {
        echo $joursFR[$jourAng] . " " . $jourNum . " " . $moisFR[$moisAng] . " " . $annee;
    } elseif ($lang == "EN") {
        echo $jourAng . " " . $jourNum . " " . $moisAng . " " . $annee;
    }  else {
        echo date("d/m/Y");
    }
}

function getIntituleFiliere($code, $filieres)
{
    foreach ($filieres as $filiere) {
        if ($filiere["CodeFiliere"] == $code) {
            return $filiere["IntituleFiliere"];
        }
    }
    return "";
}
?>