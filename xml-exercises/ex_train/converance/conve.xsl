<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/conference">
      <html>
        <head>

        </head>
        <body>
            <h1><xsl:value-of select="/conference/@code"/>----<xsl:value-of select="/conference/@city"/> </h1>
            <h1>Session table</h1>
            <table>
                <tr>
                    <th>id</th>
                    <th>title</th>
                    <th>speaker</th>
                    <th>name</th>
                    <th>min</th>
                    <th>room</th>
                </tr>
                    <xsl:for-each select="//session">
                        <tr>
                            <td><xsl:value-of select="@id"/></td>
                            <td><xsl:value-of select="title"/></td>
                            <td><xsl:value-of select="//participant[@id=current()/speaker/@ref]/name"/></td>
                            <td><xsl:value-of select="duration/@minutes"/></td>
                            <td><xsl:value-of select="room"/></td>
                        </tr>
        
                    </xsl:for-each>
            </table>
            <h1>Ticket table</h1>
             <table>
                <tr>
                    <th>ticket id</th>
                    <th>participant name</th>
                    <th>category</th>
                    <th>price</th>
                </tr>
                    <xsl:for-each select="//ticket">
                        <tr>
                            <td><xsl:value-of select="@id"/></td>
                            <td><xsl:value-of select="//participant[@id=current()/@participant]/name"/></td>
                            <td><xsl:value-of select="@category"/></td>
                            <td><xsl:value-of select="@price"/></td>
                        </tr>
        
                    </xsl:for-each>
            </table>
            <h1>total sessions:<xsl:value-of select="count(//session)"/></h1>
        </body>
      </html>  

    </xsl:template>
</xsl:stylesheet>