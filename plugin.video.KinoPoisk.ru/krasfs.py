#!/usr/bin/python
# -*- coding: utf-8 -*-

import httplib
#import re
#import sys
import os
import Cookie

import string, xbmc, xbmcgui, xbmcplugin, urllib, cookielib, xbmcaddon
#-------------------------------
import urllib, urllib2, time, random
#from time import gmtime, strftime 
#from urlparse import urlparse 

import HTMLParser 
hpar = HTMLParser.HTMLParser()
#-----------------------------------------
import socket
socket.setdefaulttimeout(50)

icon = ""
siteUrl = 'www.krasfs.ru'
httpSiteUrl = 'http://' + siteUrl
sid_file = os.path.join(xbmc.translatePath('special://temp/'), 'krasfs.cookies.sid')#'plugin.video.krasfs.ru.cookies.sid'

#h = int(sys.argv[1])


#--------------- 
cj = cookielib.FileCookieJar(sid_file) 
hr  = urllib2.HTTPCookieProcessor(cj) 
opener = urllib2.build_opener(hr) 
urllib2.install_opener(opener) 

def unescape(text): 
    try: 
        text = hpar.unescape(text) 
    except: 
        text = hpar.unescape(text.decode('utf8')) 

    try: 
        text = unicode(text, 'utf-8') 
    except: 
        text = text 

    return text 
#--------------- 
url='http://www.krasfs.ru/' 

#-- step 1 - get session cookies 
post = None 
request = urllib2.Request(url, post) 

request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)') 
request.add_header('Host',    'www.krasfs.ru') 
request.add_header('Accept', '*/*') 
request.add_header('Accept-Language', 'ru-RU') 
request.add_header('Referer',    'http://www.krasfs.ru') 

try: 
    f = urllib2.urlopen(request) 
except IOError, e: 
    if hasattr(e, 'reason'): 
        xbmc.log('We failed to reach a server. Reason: '+ e.reason) 
    elif hasattr(e, 'code'): 
        xbmc.log('The server couldn\'t fulfill the request. Error code: '+ e.code)

# ---------------------------------------

def showMessage(heading, message, times = 3000):
	xbmc.executebuiltin('XBMC.Notification("%s", "%s", %s, "%s")'%(heading, message, times, icon))

def ru(x):return unicode(x,'utf8', 'ignore')
def xt(x):return xbmc.translatePath(x)

def formtext(http):
	#http=http.replace(chr(10),"")#.replace(chr(13),"")
	http=http.replace("'",'"').replace('&nbsp;'," ")#исключить
	http=http.replace('           <',"<").replace('          <',"<").replace('         <',"<").replace('        <',"<").replace('       <',"<").replace('      <',"<").replace('     <',"<").replace('    <',"<").replace('   <',"").replace('  <',"<").replace(' <',"<")
	http=http.replace('&amp;nbsp;',"")
	#http=http.replace('</a> </td> <td align=center>',"', '").replace('</td> </tr>  <tr> <td align=left>  ',"']"+chr(10)).replace('> ',"', '")
	#http=cleartext(http)
	
	return http

def formating(str):
	str=str.strip()
	str=str.replace('%','%25')
	str=str.replace('&','%26')
	str=str.replace('?','%3F')
	str=str.replace('&','%26')
	str=str.replace('!','%21')
	str=str.replace(':','%3A')
	str=str.replace('#','%23')
	str=str.replace(',','%2C')
	str=str.replace(';','%3B')
	str=str.replace('@','%40')
	str=str.replace('(','%28')
	str=str.replace(')','%29')
	str=str.replace('"','%22')
	
	str=str.replace('а','%E0')
	str=str.replace('б','%E1')
	str=str.replace('в','%E2')
	str=str.replace('г','%E3')
	str=str.replace('д','%E4')
	str=str.replace('е','%E5')
	str=str.replace('ё','%b8')
	str=str.replace('ж','%E6')
	str=str.replace('з','%E7')
	str=str.replace('и','%E8')
	str=str.replace('й','%E9')
	str=str.replace('к','%EA')
	str=str.replace('л','%EB')
	str=str.replace('м','%EC')
	str=str.replace('н','%ED')
	str=str.replace('о','%EE')
	str=str.replace('п','%EF')
	str=str.replace('р','%F0')
	str=str.replace('с','%F1')
	str=str.replace('т','%F2')
	str=str.replace('у','%F3')
	str=str.replace('ф','%F4')
	str=str.replace('х','%F5')
	str=str.replace('ц','%F6')
	str=str.replace('ч','%F7')
	str=str.replace('ш','%F8')
	str=str.replace('щ','%F9')
	str=str.replace('ь','%FA')
	str=str.replace('ы','%FB')
	str=str.replace('ъ','%FC')
	str=str.replace('э','%FD')
	str=str.replace('ю','%FE')
	str=str.replace('я','%FF')
	
	str=str.replace('А','%C0')
	str=str.replace('Б','%C1')
	str=str.replace('В','%C2')
	str=str.replace('Г','%C3')
	str=str.replace('Д','%C4')
	str=str.replace('Е','%C5')
	str=str.replace('Ё','%A8')
	str=str.replace('Ж','%C6')
	str=str.replace('З','%C7')
	str=str.replace('И','%C8')
	str=str.replace('Й','%C9')
	str=str.replace('К','%CA')
	str=str.replace('Л','%CB')
	str=str.replace('М','%CC')
	str=str.replace('Н','%CD')
	str=str.replace('О','%CE')
	str=str.replace('П','%CF')
	str=str.replace('Р','%D0')
	str=str.replace('С','%D1')
	str=str.replace('Т','%D2')
	str=str.replace('У','%D3')
	str=str.replace('Ф','%D4')
	str=str.replace('Х','%D5')
	str=str.replace('Ц','%D6')
	str=str.replace('Ч','%D7')
	str=str.replace('Ш','%D8')
	str=str.replace('Щ','%D9')
	str=str.replace('Ь','%DA')
	str=str.replace('Ы','%DB')
	str=str.replace('Ъ','%DC')
	str=str.replace('Э','%DD')
	str=str.replace('Ю','%DE')
	str=str.replace('Я','%DF')
	str=str.replace(' ','+')
	return str

def inputbox():
	skbd = xbmc.Keyboard()
	skbd.setHeading('Поиск:')
	skbd.doModal()
	if skbd.isConfirmed():
		SearchStr = skbd.getText()
		return SearchStr
	else:
		return ""


def upd(category, sort, str):
		post = urllib.urlencode({'checkbox_ftp':'on', 'checkbox_tor':'on','word':str}) 
		request = urllib2.Request('http://krasfs.ru/search.php?key=newkey')#url, post)

		request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)') 
		request.add_header('Host',    'www.krasfs.ru') 
		request.add_header('Accept', '*/*') 
		request.add_header('Accept-Language', 'ru-RU') 
		request.add_header('Referer',    'http://www.krasfs.ru') 

		try: 
			f = urllib2.urlopen(request) 
			html = f.read()
			html = html.replace(chr(10),"")
			n=html.find("<newkey>")
			k=html.find("</newkey>")
			key = html[n+8:k]
		except IOError, e: 
			if hasattr(e, 'reason'): 
				print 'We failed to reach a server. Reason: '+ e.reason
			elif hasattr(e, 'code'): 
				print 'The server couldn\'t fulfill the request. Error code: '+ e.code
			key = "59165b78-bf91-11e1-86bf-c6ab051766ba"
		
		str=str.replace(" ", "%20")
		request = urllib2.Request('http://krasfs.ru/search.php?key='+key+'&query='+str+'&out=xml&type=torrent')
		request.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)') 
		request.add_header('Host',    'www.krasfs.ru') 
		request.add_header('Accept', '*/*') 
		request.add_header('Accept-Language', 'ru-RU') 
		request.add_header('Referer',    'http://www.krasfs.ru') 

		try: 
			f = urllib2.urlopen(request) 
			html = f.read()
			html=formtext(html)
			return html
		except IOError, e: 
			if hasattr(e, 'reason'): 
				print 'We failed to reach a server.'
			elif hasattr(e, 'code'): 
				print 'The server couldn\'t fulfill the request. Error'
			return ""


def format(L):
		if L==None: 
			return ["","","","","","","","",""]
		else:
			Ln=[]
			i=0
			tmp1=''
			tmp2=''
			tmp3=''
			for itm in L:
				i+=1
				if len(itm)>6:
					if itm[:5]=="</out":
						i=0
						Ln.append([" -- ",tmp3,tmp2,tmp1])
					elif itm[:4]=="<has":
						tmp1='https://krasfs.ru/download.php?hash='+itm[6:-7]
					elif itm[:4]=="<alt":
						tmp2=itm[10:-11]
					elif itm[:6]=="<sizef":
						tmp3=itm[7:-8]
			return Ln
			
class Tracker:
	def __init__(self):
		pass

	def Search(self, text="миля", category=4):
		sort='newest'
		RL=upd(category, sort, xt(text))
		RootList=format(RL.splitlines())
		#debug(str(RootList))
		Lout=[]
		Lt=[]
		for t in RootList:
			if len(t)==4 :
				size=t[1].strip()#xt()
				n=size.find(".")
				
				if size[-4:]=="\xd0\x9c\xd0\xb1":
					size=size[:n]
					if len(size)==0:size="   -----   "
					if len(size)==1:size="    "+size+"\xd0\x9c\xd0\xb1"+"    "
					if len(size)==2:size="   "+size+"\xd0\x9c\xd0\xb1"+"   "
					if len(size)==3:size="  "+size+"\xd0\x9c\xd0\xb1"+"  "
					if len(size)==4:size=" "+size+"\xd0\x9c\xd0\xb1"+" "
				else:
					#print len(size)
					if len(size)==4:size="    "+size+"    "
					if len(size)==5:size="     "+size+"    "
					if len(size)==6:size="   "+size+"   "
					if len(size)==7:size="   "+size+"   "
					if len(size)==8:size="  "+size+"  "
					if len(size)==9:size=" "+size+" "
					if len(size)==10:size=" "+size+" "
				qual="    -----    "
				if t[2].lower().find("dvd5")>0:  qual="   DVD5   "
				if t[2].lower().find("dvd9")>0:  qual="   DVD9   "
				if t[2].lower().find("bdrip")>0: qual="  BDRip   "
				if t[2].lower().find("hdrip")>0: qual="  HDRip   "
				if t[2].lower().find("bluray")>0:qual="  BluRay  "
				if t[2].lower().find("webdl")>0: qual="  WEB-DL "
				if t[2].lower().find("web-dl")>0:qual="  WEB-DL "
				if t[2].lower().find("720h")>0:  qual="    720h    "
				if t[2].lower().find("720p")>0:  qual="    720p    "
				if t[2].lower().find("1080p")>0: qual="  1080p   "
				if t[2].lower().find("1080")>0:  qual="  1080p   "
				if t[2].lower().find("dvdrip")>0:qual=" DVDRip  "
				if t[2].lower().find("ipod")>0:  qual="    iPod    "
				if t[2].lower().find("tvrip")>0: qual="   TVRip   "
				if t[2].lower().find("satrip")>0:qual="  SATRip  "
				if t[2].lower().find("camrip")>0:qual="  CAMRip "
				#print xt(t[2])
				
				tmpn=size+t[2]
				if tmpn not in Lt: Lout.append([qual,size,xt(t[2]),t[3]])
				Lt.append(tmpn)
		return Lout