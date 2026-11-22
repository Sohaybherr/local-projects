<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/event">
    <html>
      <head>
        <title>Event Details</title>
      </head>
      <body>

        <!-- TEST visuel -->
        <h1>HELLO XSLT WORKS</h1>

        <h2>
          Evenement:
          <xsl:value-of select="@code"/>
          ----
          <xsl:value-of select="@ville"/>
        </h2>

        <table border="1">
          <tr>
            <th>num</th>
            <th>nom</th>
            <th>nometa</th>
            <th>langue</th>
            <th>theme</th>
          </tr>

          <!-- langue = ang -->
          <xsl:for-each select="participant/(invite | inter)[langue='ang']">
            <tr style="color:red;font-size:large;">
              <td><xsl:value-of select="num"/></td>
              <td><xsl:value-of select="nom"/></td>
              <td><xsl:value-of select="nometa"/></td>
              <td><xsl:value-of select="langue"/></td>
              <td><xsl:value-of select="theme"/></td>
            </tr>
          </xsl:for-each>

          <!-- langue != ang -->
          <xsl:for-each select="participant/(invite | inter)[langue!='ang']">
            <tr>
              <td><xsl:value-of select="num"/></td>
              <td><xsl:value-of select="nom"/></td>
              <td><xsl:value-of select="nometa"/></td>
              <td><xsl:value-of select="langue"/></td>
              <td><xsl:value-of select="theme"/></td>
            </tr>
          </xsl:for-each>

        </table>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>

        