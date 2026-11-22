<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <title>Liste des employés</title>
            </head>
            <body>
              <h1>liste des devs</h1>
                <ul>
                   <xsl:for-each select="//employe[@poste='dev']">
                    <li>
                     <label>poste:</label> <xsl:value-of select="@poste"/> 
                      <label>salaire:</label> <xsl:value-of select="@salaire"/>
                      <label>nom:</label> <xsl:value-of select="."/>
                    </li>
                    </xsl:for-each>
                </ul>    
                <h1>max salaire</h1>
              <xsl:for-each select="//employe">
                <xsl:sort select="@salaire" data-type="number" order="descending"/>  
                <xsl:if test="position()=1">
                  <label>poste:</label> <xsl:value-of select="@poste"/> 
                  <label>salaire:</label> <xsl:value-of select="@salaire"/>
                  <label>nom:</label> <xsl:value-of select="."/>
                </xsl:if>
              </xsl:for-each>   
                <h1>Liste des employés:</h1><div>
                <xsl:for-each select="//employe">
                    <xsl:if test="@salaire > 10000">
                       <div style="color:red;"> 
                      <label>poste:</label> <xsl:value-of select="@poste"/> 
                      <label>salaire:</label> <xsl:value-of select="@salaire"/>
                      <label>nom:</label> <xsl:value-of select="."/> </div>
                    </xsl:if> 
            </xsl:for-each>  
                </div> 
                <div>
                <xsl:for-each select="//employe">
                    <xsl:if test="@salaire  &lt;=  10000">
                       <div style="color:black;"> 
                      <label>poste:</label> <xsl:value-of select="@poste"/>           
                      <label>salaire:</label> <xsl:value-of select="@salaire"/>
                      <label>nom:</label> <xsl:value-of select="."/> </div>
                    </xsl:if> 
            </xsl:for-each>  
                </div> 


            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>    