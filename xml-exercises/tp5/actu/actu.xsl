<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns="http://www.w3.org/1999/xhtml">

    <!-- Grouping des brèves par thème (Muenchian grouping) -->
    <xsl:key name="breves-par-theme" match="breve" use="@theme"/>

    <xsl:output method="xml" indent="yes" doctype-system="about:legacy-compat"/>

    <!-- Racine -->
    <xsl:template match="/actu">
        <html>
        <head>
            <title>Actualités</title>
            <meta charset="UTF-8"/>
        </head>
        <body>
            <h1>Actualités par thème</h1>

            <!-- Statistiques langues -->
            <h2>Statistiques</h2>
            <p>Brèves en français :
                <strong><xsl:value-of select="count(breve[@langue='fr'])"/></strong>
            </p>
            <p>Brèves en anglais :
                <strong><xsl:value-of select="count(breve[@langue='en'])"/></strong>
            </p>

            <!-- Groupement par thème -->
            <xsl:for-each
                select="breve[generate-id() = generate-id(key('breves-par-theme', @theme)[1])]">
                <xsl:sort select="@theme"/>

                <h2>Thème : <xsl:value-of select="@theme"/></h2>

                <!-- Toutes les brèves de ce thème -->
                <xsl:for-each select="key('breves-par-theme', @theme)">
                    <div class="breve">
                        <h3>
                            <xsl:value-of select="titre"/>
                            <span> (<xsl:value-of select="@date"/>,
                                <xsl:value-of select="@langue"/>)</span>
                        </h3>

                        <!-- Texte de la brève -->
                        <p>
                            <xsl:value-of select="normalize-space(texte)"/>
                        </p>

                        <!-- Photo si elle existe -->
                        <xsl:if test="photo">
                            <p>
                                <img src="{photo/@src}" alt="photo de la brève"/>
                            </p>
                        </xsl:if>

                        <!-- URLs transformées en liens hypertextes -->
                        <xsl:for-each select="url">
                            <p>
                                <a href="{@href}">
                                    <xsl:value-of select="."/>
                                </a>
                            </p>
                        </xsl:for-each>

                        <hr/>
                    </div>
                </xsl:for-each>
            </xsl:for-each>
        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
