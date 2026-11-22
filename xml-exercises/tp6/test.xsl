<?xml version="1.0" encoding="UTF-8"?>

 <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:output method="html" encoding="UTF-8" indent="yes"/>



<xsl:template match="/todolist">
<html>
<head>
    <title>Todo list de <xsl:value-of select="@owner"/></title>
    <style>
        body { font-family: Arial; }
        .critic { color: red; font-weight: bold; }
        img { width: 120px; }
    </style>
</head>

<body>
<h1>Todo list de <xsl:value-of select="@owner"/></h1>

<xsl:apply-templates select="todo"/>

</body>
</html>
    </xsl:template>

        <!-- ===== TODO ===== -->
        <xsl:template match="todo">
        <hr/>
        <img>
            <xsl:attribute name="src">
                <xsl:value-of select="@illustration"/>
            </xsl:attribute>
        </img>

        <h2><xsl:value-of select="title"/></h2>
        <p><strong>Date limite :</strong> <xsl:value-of select="@deadline"/></p>

        <!-- Commentaires -->
        <xsl:apply-templates select="commentaires/par"/>

        <!-- Items -->
        <ul>
            <xsl:apply-templates select="items/item"/>
        </ul>

    </xsl:template>

<!-- ===== PARAGRAPHES ===== -->
    <xsl:template match="par">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>

<!-- ===== ITEMS ===== -->
    <xsl:template match="item">
        <li>
            <xsl:if test="@level='critic'">
                <xsl:attribute name="class">critic</xsl:attribute>
            </xsl:if>
            <xsl:apply-templates/>
        </li>
    </xsl:template>

<!-- ===== BALISES INTERNES ===== -->
    <xsl:template match="important">
        <strong><xsl:apply-templates/></strong>
    </xsl:template>

    <xsl:template match="date">
        <em><xsl:apply-templates/></em>
    </xsl:template>

<xsl:template match="lien">
    <a>
        <xsl:attribute name="href">
            <xsl:value-of select="@url"/>
        </xsl:attribute>
        <xsl:apply-templates/>
    </a>
</xsl:template>

</xsl:stylesheet>
