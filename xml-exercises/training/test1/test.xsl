<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns="http://www.w3.org/1999/xhtml">
    <xsl:output method="xml" indent="yes" doctype-system="about:legacy-compat"/>
    <xsl:template match="/">
        <html>
         <head>
            <title>Liste des personnes</title>
        </head>
        <body>      
        <h1>listes personnes:</h1>
         <xsl:for-each  select="personnes/personne">
        <div>
           <p>- <xsl:value-of select="nom"/> (<xsl:value-of select="age"/>)</p> 
        </div>
             </xsl:for-each>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>