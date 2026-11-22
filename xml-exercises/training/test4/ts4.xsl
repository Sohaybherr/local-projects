<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
    <html>
        <head>

        </head>
        <body>
               <h1>table of products</h1>
    <table>
        <tr>
            <th>product</th>
            <th>t-shirt</th>
        </tr>
        <xsl:for-each select="//produit">
            <xsl:if test="@prix >100">
            <tr style="color:red;">
                <td><xsl:value-of select="."/></td>
                <td><xsl:value-of select="@prix"/></td>
            </tr>
            </xsl:if>
        </xsl:for-each>
         <xsl:for-each select="//produit">
            <xsl:if test="@prix  &lt;= 100">
            <tr style="color:black;">
                <td><xsl:value-of select="."/></td>
                <td><xsl:value-of select="@prix"/></td>
            </tr>
            </xsl:if>
        </xsl:for-each>
    </table>
    <h1>most expensive</h1>
    <xsl:for-each select="//produit">
        <xsl:sort select="@prix" data-type="number" order="descending"/>
        <xsl:if test="position()=1">
            <label>product:</label> <xsl:value-of select="."/>
            <label>price:</label> <xsl:value-of select="@prix"/>
        </xsl:if>
    </xsl:for-each>
        <h1>cheapest</h1>
    <xsl:for-each select="//produit">
        <xsl:sort select="@prix" data-type="number" order="descending"/>
        <xsl:if test="position()=3">
            <label>product:</label> <xsl:value-of select="."/>
            <label>price:</label> <xsl:value-of select="@prix"/>
        </xsl:if>
    </xsl:for-each>
    <h1>to cheapest</h1>
        <xsl:for-each select="//produit">
        <xsl:sort select="@prix" data-type="number" order="descending"/>
            <label>product:</label> <xsl:value-of select="."/>
            <label>price:</label> <xsl:value-of select="@prix"/><br></br>
    </xsl:for-each>
    

        </body>
    </html>
   

</xsl:template>

</xsl:stylesheet>    