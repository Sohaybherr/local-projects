<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/store">
        <html>
            <head>

            </head>
            <body>
                <h1><xsl:value-of select="@name"/> - <xsl:value-of select="@location"/></h1>
                <table>
                    <tr>
                        <th>SKU</th>
                        <th>Product Name</th>
                        <th>Category</th>
                        <th>Price</th>
                        <th>Currency</th>
                        <th>Stock</th>
                    </tr>
                    <xsl:for-each select="catalog/product">
                       <xsl:sort select="price" data-type="number" order="ascending"/>
                        <tr>
                            <td><xsl:value-of select="@sku"/></td>
                            <td><xsl:value-of select="label"/></td>
                            <td><xsl:value-of select="@category"/></td>
                            <td><xsl:value-of select="price"/></td>
                            <td><xsl:value-of select="price/@currency"/></td>
                            <td><xsl:value-of select="stock"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
                <table>
                    <tr>
                        <th>order num</th>
                        <th>date</th>
                        <th>customer</th>
                        <th>total items</th>
                        <th>paid</th>
                        
                    </tr>
                    <xsl:for-each select="orders/order">
                        <tr>
                            <td><xsl:value-of select="@no"/></td>
                            <td><xsl:value-of select="@date"/></td>
                            <td><xsl:value-of select="/store/customers/costumer[@id = current()/@customer]/fullname"/></td>
                            <td><xsl:value-of select="sum(items/item/@quantity)"/></td>
                           <xsl:choose>
                               <xsl:when test="@paid='yes'">
                                   <td>Yes</td>
                               </xsl:when>
                               <xsl:otherwise>
                                   <td>No</td>
                               </xsl:otherwise>
                            </xsl:choose>
                        </tr>
                    </xsl:for-each>
                </table>    
                <footer>
                    <h2>Total Products: <xsl:value-of select="count(catalog/product)"/></h2>
                    <h2>Total Orders: <xsl:value-of select="count(orders/order)"/></h2>
                </footer>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
