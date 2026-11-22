<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Catalogue des produits</title>
            </head>
            <body>
                <h1>Liste des produits:</h1>
                <table>
                    <tr>
                        <th>Produit</th>
                        <th>Prix</th>
                    </tr>
                <xsl:for-each select="catalogue/produit">
                   
                           <tr>
                               <td><xsl:value-of select="."/></td>
                               <td><xsl:value-of select="@prix"/></td>
                           </tr>
                </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>