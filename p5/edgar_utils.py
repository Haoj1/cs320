import pandas as pd
import re
import netaddr
from bisect import bisect

html = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Last-Modified" content="Fri, 12 Feb 2016 00:05:37 GMT" />
<title>EDGAR Filing Documents for 0001050470-16-000051</title>
<link rel="stylesheet" type="text/css" href="/include/interactive.css" />
</head>
<body style="margin: 0">
<!-- SEC Web Analytics - For information please visit: https://www.sec.gov/privacy.htm#collectedinfo -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-TD3BKV"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-TD3BKV');</script>
<!-- End SEC Web Analytics -->
<noscript><div style="color:red; font-weight:bold; text-align:center;">This page uses Javascript. Your browser either doesn't support Javascript or you have it turned off. To see this page as it is meant to appear please use a Javascript enabled browser.</div></noscript>
<!-- BEGIN BANNER -->
<div id="headerTop">
   <div id="Nav"><a href="/index.htm">Home</a> | <a href="/cgi-bin/browse-edgar?action=getcurrent">Latest Filings</a> | <a href="javascript:history.back()">Previous Page</a></div>
   <div id="seal"><a href="/index.htm"><img src="/images/sealTop.gif" alt="SEC Seal" border="0" /></a></div>
   <div id="secWordGraphic"><img src="/images/bannerTitle.gif" alt="SEC Banner" /></div>
</div>
<div id="headerBottom">
   <div id="searchHome"><a href="/edgar/searchedgar/webusers.htm">Search the Next-Generation EDGAR System</a></div>
   <div id="PageTitle">Filing Detail</div>
</div>
<!-- END BANNER -->


<!-- BEGIN BREADCRUMBS -->
<div id="breadCrumbs">
   <ul>
      <li><a href="/index.htm">SEC Home</a> &#187;</li>
      <li><a href="/edgar/searchedgar/webusers.htm">Search the Next-Generation EDGAR System</a> &#187;</li>
      <li><a href="/edgar/searchedgar/companysearch.html">Company Search</a> &#187;</li>
      <li class="last">Current Page</li>
   </ul>
</div>
<!-- END BREADCRUMBS -->

<div id="contentDiv">
<!-- START FILING DIV -->
<div id="formDiv">
   <div id="formHeader">
      <div id="formName">
         <strong>Form SC 13G</strong> - Statement of acquisition of beneficial ownership by individuals: 
      </div>
      <div id="secNum">
         <strong><acronym title="Securities and Exchange Commission">SEC</acronym> Accession <acronym title="Number">No.</acronym></strong> 0001050470-16-000051
      </div>
   </div>
   <div class="formContent">
      <div class="formGrouping">
         <div class="infoHead">Filing Date</div>
         <div class="info">2016-02-12</div>
         <div class="infoHead">Accepted</div>
         <div class="info">2016-02-11 19:05:37</div>
         <div class="infoHead">Documents</div>
         <div class="info">1</div>
      </div>
      <div style="clear:both"></div>
   </div>
</div>
<!-- END FILING DIV -->
<!-- START DOCUMENT DIV -->
<div id="formDiv">
   <div style="padding: 0px 0px 4px 0px; font-size: 12px; margin: 0px 2px 0px 5px; width: 100%; overflow:hidden">
      <p>Document Format Files</p>
      <table class="tableFile" summary="Document Format Files">
         <tr>
            <th scope="col" style="width: 5%;"><acronym title="Sequence Number">Seq</acronym></th>
            <th scope="col" style="width: 40%;">Description</th>
            <th scope="col" style="width: 20%;">Document</th>
            <th scope="col" style="width: 10%;">Type</th>
            <th scope="col">Size</th>
         </tr>
         <tr>
            <td scope="row">1</td>
            <td scope="row">LSV13G123115MEDALLION.TXT</td>
            <td scope="row"><a href="/Archives/edgar/data/1000209/000105047016000051/lsv13g123115medallion.txt">lsv13g123115medallion.txt</a></td>
            <td scope="row">SC 13G</td>
            <td scope="row">8314</td>
         </tr>
         <tr class="blueRow">
            <td scope="row">&nbsp;</td>
            <td scope="row">Complete submission text file</td>
            <td scope="row"><a href="/Archives/edgar/data/1000209/000105047016000051/0001050470-16-000051.txt">0001050470-16-000051.txt</a></td>
            <td scope="row">&nbsp;</td>
            <td scope="row">9803</td>
         </tr>
      </table>	
   </div>
</div>
<!-- END DOCUMENT DIV -->
<!-- START FILER DIV -->
<div id="filerDiv">
   <div class="mailer">Mailing Address
      <span class="mailerAddress">437 MADISON AVENUE</span>
      <span class="mailerAddress">38TH FLOOR</span>
      <span class="mailerAddress">
NEW YORK NY 10022      </span>
   </div>
   <div class="mailer">Business Address
      <span class="mailerAddress">437 MADISON AVE 38 TH FLOOR</span>
      <span class="mailerAddress">
NEW YORK NY 10022      </span>
      <span class="mailerAddress">2123282153</span>
   </div>
<div class="companyInfo">
  <span class="companyName">MEDALLION FINANCIAL CORP (Subject)
 <acronym title="Central Index Key">CIK</acronym>: <a href="/cgi-bin/browse-edgar?CIK=0001000209&amp;action=getcompany">0001000209 (see all company filings)</a></span>
<p class="identInfo"><acronym title="Internal Revenue Service Number">IRS No.</acronym>: <strong>043291176</strong> | State of Incorp.: <strong>DE</strong> | Fiscal Year End: <strong>1231</strong><br />Type: <strong>SC 13G</strong> | Act: <strong>34</strong> | File No.: <a href="/cgi-bin/browse-edgar?filenum=005-48473&amp;action=getcompany"><strong>005-48473</strong></a> | Film No.: <strong>161413579</strong><br /><acronym title="Standard Industrial Code">SIC</acronym>: <b><a href="/cgi-bin/browse-edgar?action=getcompany&amp;SIC=6199&amp;owner=include">6199</a></b> Finance Services<br />Office of Finance</p>
</div>
<div class="clear"></div>
</div>
<div id="filerDiv">
   <div class="mailer">Mailing Address
      <span class="mailerAddress">155 NORTH WACKER DRIVE</span>
      <span class="mailerAddress">SUITE 4600</span>
      <span class="mailerAddress">
CHICAGO IL 60606      </span>
   </div>
   <div class="mailer">Business Address
      <span class="mailerAddress">155 NORTH WACKER DRIVE</span>
      <span class="mailerAddress">SUITE 4600</span>
      <span class="mailerAddress">
CHICAGO IL 60606      </span>
      <span class="mailerAddress">312-460-2443</span>
   </div>
<div class="companyInfo">
  <span class="companyName">LSV ASSET MANAGEMENT (Filed by)
 <acronym title="Central Index Key">CIK</acronym>: <a href="/cgi-bin/browse-edgar?CIK=0001050470&amp;action=getcompany">0001050470 (see all company filings)</a></span>
<p class="identInfo"><acronym title="Internal Revenue Service Number">IRS No.</acronym>: <strong>232772200</strong> | State of Incorp.: <strong>DE</strong> | Fiscal Year End: <strong>1231</strong><br />Type: <strong>SC 13G</strong></p>
</div>
<div class="clear"></div>
</div>
<!-- END FILER DIV -->
</div>"""

ips = pd.read_csv("ip2location.csv")
low = ips['low']

def lookup_region(ip):
    
    ipaddr = ip
    ipaddr = re.sub(r'[a-zA-Z]', r'0', ipaddr)
    ip_int = int(netaddr.IPAddress(ipaddr))
    idx = bisect(low, ip_int) - 1
    return ips.iloc[idx]['region']

class Filing:
    def __init__(self, html):
        # find the dates
        dates  = re.findall(r"19\d\d-\d\d-\d\d|20\d\d-\d\d-\d\d", html)
        # remove the invalid dates
        # for date in dates:
        #     if int(date[8:10]) > 31:
        #         dates.remove(date)

        # for date in dates:
        #     if int(date[5:7]) > 12:
        #         dates.remove(date)
        self.dates = dates
        
        sic = re.findall(r"SIC=(.{4})", html)
        if len(sic) == 0:
            self.sic = None
        else:
            self.sic = int(sic[0])
        
        addresses = []
        for addr_html in re.findall(r'<div class="mailer">([\s\S]+?)</div>', html):
            lines = []
            for line in re.findall(r'<span class="mailerAddress">([\s\S]+?)</span>', addr_html):
                line =line.replace('\n', '')
                if line != None:
                  lines.append(line.strip())
            if lines:
                addresses.append('\n'.join(lines))
        self.addresses = addresses
        

    def state(self):
        for address in self.addresses:
            state = re.findall(r'[A-Z]{2} \d{5}',address)
            if len(state) != 0:
                return state[0][0:2]
        return None


# ipaddr = "1.1.1.abc"
# ipaddr = re.sub(r'[a-zA-Z]', r'0', ipaddr)
# int_IP = int(netaddr.IPAddress(ipaddr))
# idx = bisect(low, int_IP)
# print(ips.iloc[idx-1])

# filing  = Filing(html)
# print(filing.addresses)
# for addr_html in re.findall(r'<div class="mailer">([\s\S]+?)</div>', html):
#     lines = []
#     for line in re.findall(r'<span class="mailerAddress">([\s\S]+?)</span>', addr_html):
#         lines.append(line.strip())
#     print("\n".join(lines))
#     print()
