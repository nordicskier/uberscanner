import tkinter
from time import sleep
from os import remove
from os import listdir
from os import chdir
from os import getcwd
from os import rename
from subprocess import Popen
from subprocess import call
import shutil

class UberScanner(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent=parent
        self.initialize()

    def initialize(self):
        self.grid()
        #spacers
        blank0=tkinter.Canvas(height=5,width=15)
        blank0.grid(column=0,row=0)        
        blank4=tkinter.Canvas(height=20,width=50)
        blank4.grid(column=2,row=1)
        blank5=tkinter.Canvas(height=20,width=15)
        blank5.grid(column=4,row=1)
        blank6=tkinter.Canvas(height=10,width=15)
        blank6.grid(column=5,row=9)
        blank7=tkinter.Canvas(height=10, width =15)
        blank7.grid(column=5, row=11)
        blank8=tkinter.Canvas(height=10,width=10)
        blank8.grid(column=1,row=12)
        
        button_port=tkinter.Button(self,text=u'Check Ports',relief='groove',
                                   command=self.OnPortClick, justify='center',\
                                   width=30)
        button_port.grid(column=1,row=1,sticky='W')

        button_begin=tkinter.Button(self,text=u'Begin Log',relief='groove',
                                    command=self.OnBeginClick,justify='center',\
                                    width=30)
        button_begin.grid(column=1,row=3,sticky='W')


        button_end=tkinter.Button(self,text=u'End Log',relief='groove',
                                  command=self.OnEndClick,\
                                  justify='center',width=30)
        button_end.grid(column=1,row=5,sticky='W')
    
        button_sep=tkinter.Button(self,text=u'Parse Scan Log',relief='groove',
                                  command=self.OnSepClick, justify='center',\
                                  width=30)
        button_sep.grid(column=1,row=7)

        button_html=tkinter.Button(self, text=u'Generate HTML files',\
                                   relief='groove',command=self.OnHtmlClick,\
                                   justify='center',width=30)
        button_html.grid(column=1, row=9)

        button_csv=tkinter.Button(self, text=u'Generate CSV files',\
                                  relief='groove', command=self.OnCsvClick,\
                                  justify='center',width=30)
        button_csv.grid(column=1,row=11)

        servlabel=tkinter.Label(self,text=u'Server:')
        servlabel.grid(column=0,row=13)

        serv=tkinter.Entry(self, width=36)
        serv.grid(column=1, row=13,sticky='W')
        serv.insert(0,'liberty.starsonata.com')
        self.server=serv.get()
        

        ren_opt=tkinter.Label(self,text=u'Search and rename for the following:')
        ren_opt.grid(column=5,row=1)
        
        self.ada=tkinter.IntVar()
        self.bacta=tkinter.IntVar()
        self.dm=tkinter.IntVar()
        self.energon=tkinter.IntVar()
        self.fb=tkinter.IntVar()
        self.plat=tkinter.IntVar()
        self.rubi=tkinter.IntVar()
        self.allcom=tkinter.IntVar()
        self.bule=tkinter.IntVar()
        self.abadi=tkinter.IntVar()
        self.faranji=tkinter.IntVar()
        self.unt=tkinter.IntVar()
        self.mzungu=tkinter.IntVar()
        self.kikale=tkinter.IntVar()
        self.vazaha=tkinter.IntVar()
        self.golagoay=tkinter.IntVar()
        self.allcom=tkinter.IntVar()
        
        ada=tkinter.Checkbutton(self,text=u'Adamantium', variable=self.ada)
        ada.grid(column=5,row=2,sticky='W')
        bacta=tkinter.Checkbutton(self,text=u'Bacta', variable= self.bacta)
        bacta.grid(column=5,row=3,sticky='W')
        DM=tkinter.Checkbutton(self,text=u'Dark Matter', variable=self.dm)
        DM.grid(column=5,row=4,sticky='W')
        energon=tkinter.Checkbutton(self,text=u'Energon', variable=self.energon)
        energon.grid(column=5,row=5,sticky='W')
        FB=tkinter.Checkbutton(self,text=u'Frozen Blob', variable=self.fb)
        FB.grid(column=5,row=6,sticky='W')
        plat=tkinter.Checkbutton(self,text=u'Platinum', variable=self.plat)
        plat.grid(column=5,row=7,sticky='W')
        rub=tkinter.Checkbutton(self,text=u'Rubicite', variable=self.rubi)
        rub.grid(column=5,row=8,sticky='W')
        allc=tkinter.Checkbutton(self, text=u'All of the above',\
                                 variable=self.allcom, relief='groove')
        allc.grid(column=5, row=9, sticky='W')


        bule=tkinter.Checkbutton(self,text=u'Ruins of Bule', variable=self.bule)
        bule.grid(column=6,row=2,sticky='W')
        abadi=tkinter.Checkbutton(self,text=u'Ruins of Bule Abadi', variable=self.abadi)
        abadi.grid(column=6,row=3,sticky='W')
        far=tkinter.Checkbutton(self,text=u'Ruins of Faranji', variable=self.faranji)
        far.grid(column=6,row=4,sticky='W')
        unt=tkinter.Checkbutton(self,text=u'Ruins of Unt Faranji', variable=self.unt)
        unt.grid(column=6,row=5,sticky='W')
        mzungu=tkinter.Checkbutton(self,text=u'Ruins of Mzungu',variable=self.mzungu)
        mzungu.grid(column=6,row=6,sticky='W')
        kikale=tkinter.Checkbutton(self,text=u'Ruins of Kikale Mzungu',\
                                   variable=self.kikale)
        kikale.grid(column=6,row=7,sticky='W')
        vaz=tkinter.Checkbutton(self,text=u'Ruins of Vazaha',variable=self.vazaha)
        vaz.grid(column=6,row=8,sticky='W')
        gola=tkinter.Checkbutton(self,text=u'Ruins of Golagoay Vazaha',\
                                 variable=self.golagoay)
        gola.grid(column=6,row=9,sticky='W')

        rename=tkinter.Button(self,text=u'Rename Files',\
                              command=self.OnRenameClick, justify='center', width=20)
        rename.grid(column=5,row=10,sticky='W')
        

        
    def OnPortClick(self): #will contain a call to run 0_list.bat or equivalent
        dadap=listdir('tools\\')
        adap=0
        if 'adapter.txt' in dadap:
            ad=open('tools\\adapter.txt','r')
            adap=ad.readline()
        else:
            for n in range(1,10):
                windump='tools\WinDump.exe -Xs 1514 -w dump%s.log -i %s '\
                         'src %s' % (n,n,self.server)       
                p=Popen(windump)
                sleep(1)
                p.kill()
            td=listdir()
            direct=0
            for nn in range(len(td)):
                if td[nn].endswith('.log') and td[nn].startswith('dump'):
                    direct+=1
            for k in range(1,direct):
                fopen='dump%s.log' % str(k)
                file=open(fopen,'r',encoding='latin-1')
                line=file.readline()
                line2=file.readline()
                if line!='' and line2!='':
                    adap=k
                file.close()
            
            for j in range(1,direct):
                tr='dump%s.log' % str(j)
                remove(tr)
        
            afile=open('tools\\adapter.txt','w')
            afile.write(str(adap))
            afile.close()
        self.adapter=adap
        
    def OnBeginClick(self): #will contain a call to run 1_dump.bat or equivalent
        dadap=listdir('tools\\')
        if 'adapter.txt' in dadap:
            ad=open('tools\\adapter.txt','r')
            self.adapter=ad.readline()
        op='tools\WinDump.exe -Xs 1514 -w ss_dump.log -i %s'\
            ' src %s' % (self.adapter,self.server)
        self.pp=Popen(op)
        #for now this will need to be closed on the window with ctrl+C
        
    def OnEndClick(self): #will contain a call to end 1_dump.bat
        self.pp.kill()
    
    def OnSepClick(self): #will contain call to galaxy_seperate.py
        #chdir('..')
        f=open('ss_dump.log','r',encoding='latin-1')
        f2=open('total_scan.txt','w')
        line='not empty'

        while line!='':
            #find 'Entering Galaxy.....'
            line=f.readline()
            gal_ent=line.find('Entering galaxy')
            if gal_ent!=-1:
                line2=line[gal_ent:len(line)]
                e=line2.find('\x00')
                galaxy=line2[:e]+'\n'
                f2.write(galaxy)
            scan=line.find('Scan:')
            if scan!=-1:
                line3=line[scan:len(line)]
                dot=line3.find('\x00')
                fscan=line3[:dot]+'\n'
                f2.write(fscan)
        #end

        f.close()
        f2.close()

        del line
        del line2
        del line3

        fid=open('total_scan.txt','r');
        line='not empty'
        count=0

        while line!='':
            count+=1
            line=fid.readline()
            loc=fid.tell()
            line2=fid.readline()
            fid.seek(loc)
            if count==1 and line.find('Scan')!=-1:
                f2=open('UnknownGalaxy.txt','w')
            elif line.find('galaxy')!=-1 and line2.find('galaxy')==-1:
                try:
                    f2.close()
                except:
                    pass
                name_list=line.split()
                fname=''
                for n in range(2,len(name_list)):
                    fname+=name_list[n]
                    if len(name_list)-(n+1)!=0:
                        fname+='_'
                fname+='.txt'
                f2=open(fname,'w')
            elif line.find('galaxy')==-1:
                f2.write(line)
        
        f2.close()
        fid.close()
        remove('total_scan.txt')
        src=listdir()
        for files in src:
            if files.endswith('.txt'):
                try:
                    shutil.move(files,'scans\\')
                except:
                    remove(files)
    def OnRenameClick(self):
        dirloc=getcwd()
        if dirloc[-5:]!='scans':
            chdir('scans\\')
        files=listdir()
        for k in range(len(files)):
            gal=files[k]
            oldgal=gal
            fid=open(gal,'r')
            line='not empty'
            while line!='':
                line=fid.readline()
                if self.allcom.get()==1:
                    if line.find('Adamantium')!=-1 or line.find('Dark Matter')\
                       !=-1 or line.find('Frozen Blob')!=-1 or line.find('Energon')\
                       !=-1 or line.find('Rubicite')!=-1 or line.find('Platinum')\
                       !=-1 or line.find('Bacta')!=-1:
                        if gal.find('Commods')==-1:
                            gal='Commods_'+gal
                if self.ada.get()==1 and self.allcom.get()==0:
                    if line.find('Adamantium')!=-1:
                        if gal.find('Ada')==-1:
                            gal='Ada_'+gal
                if self.dm.get()==1 and self.allcom.get()==0:
                    if line.find('Dark Matter')!=-1:
                        if gal.find('DM')==-1:
                            gal='DM_'+gal
                if self.fb.get()==1 and self.allcom.get()==0:
                    if line.find('Frozen Blob')!=-1:
                        if gal.find('FB')==-1:
                            gal='FB_'+gal
                if self.energon.get()==1 and self.allcom.get()==0:
                    if line.find('Energon')!=-1:
                        if gal.find('Energon')==-1:
                            gal='Energon_'+gal
                if self.rubi.get()==1 and self.allcom.get()==0:
                    if line.find('Rubicite')!=-1:
                        if gal.find('Rubi')==-1:
                            gal='Rubi_'+gal
                if self.plat.get()==1 and self.allcom.get()==0:
                    if line.find('Platinum')!=-1:
                        if gal.find('Plat')==-1:
                            gal='Plat_'+gal
                if self.bacta.get()==1 and self.allcom.get()==0:
                    if line.find('Bacta')!=-1:
                        if gal.find('Bacta')==-1:
                            gal='Bacta_'+gal
                if self.faranji.get()==1:
                    if line.find('of Faranji')!=-1:
                        if gal.find('Faranji')==-1:
                            gal='Faranji_'+gal
                if self.mzungu.get()==1:
                    if line.find('of Mzungu')!=-1:
                        if gal.find('Mzungu')==-1:
                            gal='Mzungu_'+gal
                if self.bule.get()==1:
                    if line.find('Bule')!=-1 and line.find('Bule Abadi')==-1:
                        if gal.find('Bule')==-1:
                            gal='Bule_'+gal
                if self.vazaha.get()==1:
                    if line.find('of Vazaha')!=-1:
                        if gal.find('Vazaha')==-1:
                            gal='Vazaha_'+gal
                if self.abadi.get()==1:
                    if line.find('Abadi')!=-1:
                        if gal.find('Abadi')==-1:
                            gal='Abadi_'+gal
                if self.unt.get()==1:
                    if  line.find('Unt')!=-1:
                        if gal.find('Unt')==-1:
                            gal='Unt_'+gal
                if self.kikale.get()==1:
                    if line.find('Kikale')!=-1:
                        if  gal.find('Kikale')==-1:
                            gal='Kikale_'+gal
                if self.golagoay.get()==1:
                    if line.find('Golagoay')!=-1:
                        if  gal.find('Golagoay')==-1:
                            gal='Golagoay_'+gal
            fid.close()
            if oldgal.find(gal)==-1:
                rename(oldgal,gal)
                
    def OnCsvClick(self):
        def suitstuff(string,condition1,condition2, condition3):
            if string.find(condition1)!=-1:
                var=condition1
            elif string.find(condition2)!=-1:
                var=condition2
            elif string.find(condition3)!=-1:
                var=condition3
            else:
                pass
            return var
        def moresuitstuff(line):
    
            grav=suitstuff(line,'Heavy','Normal','Low')
            temp=suitstuff(line,'Blistering','Frozen','Temperate')
            atmos=suitstuff(line,'Gaseous','Noxious','Terran')

            suit=0
            if grav=='Heavy':
                x1=0.5
            elif grav=='Low':
                x1=0.75
            else:
                x1=1.0
            if temp=='Blistering':
                x2=0.5
            elif temp=='Frozen':
                x2=0.75
            else:
                x2=1.0
            if atmos=='Gaseous':
                x3=0.5
            elif atmos=='Noxious':
                x3=0.75
            else:
                x3=1.0
            suit=int(x1*x2*x3*100)
            if suit>125:
                suit=125
            return (grav,temp,atmos,suit)
        cwr=open('csv\\scans.txt','w')
        cwr.write('Galaxy,Type,Name,Grav,Temp,Atmos,Suit\n')
        dirloc=getcwd()
        if dirloc[-5:]!='scans':
            chdir('scans\\')
        files=listdir()
        for n in range(len(files)):
            cread=open(files[n],'r')
            gn=files[n]
            gn=gn[:-4]
            namelist=gn.split('_')
            count=0
            fulllist=['commods','ada','dm','fb','energon','rubi','plat',\
                      'bacta','faranji','mzungu','bule','vazaha','abadi',\
                      'unt','kikale','golagoay']
            for n in range(len(namelist)):
                if namelist[n].lower() in fulllist:
                    count+=1
            gn=''
            for k in range(count,len(namelist)):
                gn+=namelist[k]+' '
            for line in cread:
                i1=line.find('[')+1
                i2=line.find(']')
                sbn=line[i1:i2]
                line2=line[i2+2:]
                if line.find('Gravity')!=-1:
                    sbt='planet'
                    parts=line2.split('. ')
                    if line.find('Colony')==-1:
                        commods=parts[1]
                    else:
                        commods=parts[1]
                        commods=commods[23:]
                        sp=commods.find(' ')+1
                        commods=commods[sp:]
                    (grav, temp, atmos, suit)=moresuitstuff(parts[0])
                elif line.find('Gravity')==-1:
                    sbt='moon'
                    commods=line2
                    grav=''
                    temp=''
                    atmos=''
                    suit=''
                towrite='%s,%s,%s,%s,%s,%s,%s,%s' %\
                         (gn,sbt,sbn,grav,temp,atmos,suit,commods)
                cwr.write(towrite)
            cread.close()
        cwr.close()
        rename('..\\csv\\scans.txt','..\\csv\\scans.csv')

    def OnHtmlClick(self):
        dirloc=getcwd()
        if dirloc[-5:]!='scans':
            chdir('scans\\')
        scanlist=listdir()
        def suitstuff(string,condition1,condition2, condition3):
            if string.find(condition1)!=-1:
                var=condition1
            elif string.find(condition2)!=-1:
                var=condition2
            elif string.find(condition3)!=-1:
                var=condition3
            else:
                pass
            return var
        def moresuitstuff(line):
            
            grav=suitstuff(line,'Heavy','Normal','Low')
            temp=suitstuff(line,'Blistering','Frozen','Temperate')
            atmos=suitstuff(line,'Gaseous','Noxious','Terran')

            suit=0
            if grav=='Heavy':
                x1=0.5
            elif grav=='Low':
                x1=0.75
            else:
                x1=1.0
            if temp=='Blistering':
                x2=0.5
            elif temp=='Frozen':
                x2=0.75
            else:
                x2=1.0
            if atmos=='Gaseous':
                x3=0.5
            elif atmos=='Noxious':
                x3=0.75
            else:
                x3=1.0
            suit=int(x1*x2*x3*100)
            if suit>125:
                suit=125
            return (grav,temp,atmos,suit)
        def suitshort(string):
            ssuit=''
            if string.find('Low')!=-1:
                ssuit+='L'
            elif string.find('Normal')!=-1:
                ssuit+='N'
            else:
                ssuit+='H'
            if string.find('Blistering')!=-1:
                ssuit+='B'
            elif string.find('Frozen')!=-1:
                ssuit+='F'
            else:
                ssuit+='T'
            if string.find('Gaseous')!=-1:
                ssuit+='G'
            elif string.find('Noxious')!=-1:
                ssuit+='N'
            else:
                ssuit+='T'
            return ssuit
        def commods_parse(string):
            com1=''
            amount1=''
            if string.lower().find('loads')!=-1:
                amount1=string[0:9]
                com1=string[9:]
            elif string.lower().find('plenty')!=-1:
                amount1=string[0:10]
                com1=string[10:]
            elif string.lower().find('lot')!=-1:
                amount1=string[:9]
                com1=string[9:]
            elif string.lower().find('bunch')!=-1:
                amount1=string[:11]
                com1=string[11:]
            elif string.lower().find('bit')!=-1:
                amount1=string[:9]
                com1=string[9:]
            elif string.lower().find('little')!=-1:
                amount1=string[:9]
                com1=string[9:]
            elif string.lower().find('smidgin')!=-1:
                amount1=string[:13]
                com1=string[13:]
            else:
                pass
            return (amount1,com1)
        def num_amount(amount2):
            if amount2.lower().find('loads')!=-1:
                nums='65-128'
            elif amount2.lower().find('plenty')!=-1:
                nums='33-64'
            elif amount2.lower().find('lot')!=-1:
                nums='17-32'
            elif amount2.lower().find('bunch')!=-1:
                nums='9-16'
            elif amount2.lower().find('bit')!=-1:
                nums='5-8'
            elif amount2.lower().find('little')!=-1:
                nums='3-4'
            else:
                nums='1-2'
            return nums
        def color(commod):
            c=''
            if commod=='Nuclear Waste' or commod=='Silicon' or commod=='Metals' \
               or commod=='Space Oats' \
               or commod=='Baobabs':
                c='#F5F5F5'
            elif commod=='Petroleum' or commod=='Vis' or commod=='Jelly Beans' \
                 or commod=='Copper' \
                 or commod=='Tin' or commod=='Silver' or commod=='Titanium' \
                 or commod=='Psion Icicles':
                c='#3399FF'
            elif commod=='Diamond' or commod=='Quantumum' or commod=='Alien Bacteria'\
                 or commod=='Enriched Nuclear Material' or commod=='Laconia' \
                 or commod=='Plasma Crystals' or commod=='Gold':
                c='#CC9933'
            elif commod=='Fermium' or commod=='Energon' or commod=='Dark Matter' \
                 or commod=='Frozen Blob' or commod=='Adamantium' \
                 or commod=='Rubcite' or commod=='Platinum' \
                 or commod=='Ablution Crystals' or commod=='Bacta':
                c='#FF3366'
            elif commod=='Atmospheric Disturbances' or commod=='Trobbles' \
                 or commod=='Astral Worms' \
                 or commod=="Dragon's Roosts":
                c='Plum'
            else:
                pass
            return c
        for n in range(len(scanlist)):
            name=scanlist[n]
            direct='..\\pages\\%s.html' % name[:-4]
            html=open(direct, 'w')
            #style, incoming
            html.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional'\
                       '//EN" "http://www.w3.org/TR/html4/loose.dtd">\n')
            html.write('<html>\n')
            html.write('<head>\n')
            html.write('<meta http-equiv="Content-Type" content="text/html; '\
                       'charset=iso-8859-1">\n')
            html.write('<META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">\n')
            html.write('<title>%s</title>\n\n' % name[:-4])
            html.write('<style type="text/css">\n\n')
            html.write('.xsamounttip\n')
            html.write('{\n')
            html.write('    display: none;\n')
            html.write('    position: absolute;\n')
            html.write('    top: 0;\n')
            html.write('    left: 0;\n')
            html.write('    z-index: 2;\n\n')
            html.write('    font: normal 8pt sans-serif;\n')
            html.write('    padding: 2px;\n')
            html.write('    border: solid 1px;\n')
            html.write('    width: 50px;\n')
            html.write('    background-color: #2F4F4F;\n')
            html.write('    white-space: nowrap;\n')
            html.write('}\n\n')
            html.write('.xstooltip\n')
            html.write('{\n')
            html.write('    display: none;\n')
            html.write('    position: absolute;\n')
            html.write('    top: 0;\n')
            html.write('    left: 0;\n')
            html.write('    z-index: 2;\n\n')
            html.write('    font: normal 8pt sans-serif;\n')
            html.write('    padding: 3px;\n')
            html.write('    border: solid 1px;\n')
            html.write('    width: 180px;\n')
            html.write('    background-color: #2F4F4F;\n')
            html.write('    white-space: nowrap;\n')
            html.write('}\n\n')
            html.write('.xstooltiphead\n')
            html.write('{\n')
            html.write('    text-align: center;\n')
            html.write('}\n\n')
            html.write('.xsamounttip\n')
            html.write('{\n')
            html.write('    text-align: center;\n')
            html.write('}\n\n')
            html.write('table {\n')
            html.write('    border-left: 1px solid gray;\n')
            html.write('    border-right: 1px solid gray;\n')
            html.write('    border-bottom: 1px solid gray;\n')
            html.write('}\n\n')
            html.write('th {\n')
            html.write('    font-size: 10px;\n')
            html.write('    border-top: 1px solid gray;\n')
            html.write('}\n\n')
            html.write('td, body {\n')
            html.write('    background: #333;\n')
            html.write('    font-family: verdana, sans-serif;\n')
            html.write('    font-size: 10px;\n')
            html.write('    color: #fff;\n')
            html.write('}\n\n')
            html.write('tr.p td {\n')
            html.write('    border-top: 1px solid gray;\n')
            html.write('}\n\n')
            html.write('td.m {\n')
            html.write('    border-top: 1px solid gray;\n')
            html.write('    padding-left: 20px;\n')
            html.write('}\n\n')
            html.write('td.m2 {\n')
            html.write('    border-top: 1px solid gray;\n')
            html.write('}\n\n')
            html.write('DIV.suit:hover {\n')
            html.write('    color: red;\n')
            html.write('}\n\n')
            html.write('SPAN.a {\n')
            html.write('  color: #A9A9A9;\n')
            html.write('  font-size: 9px;\n')
            html.write('}\n\n')
            html.write('SPAN.a:hover {\n')
            html.write('    color: #bbb;\n')
            html.write('}\n\n')
            html.write('SPAN.c {\n')
            html.write('    color: #3CB371;\n')
            html.write('    font-weight: bold;\n')
            html.write('}\n\n')
            html.write('A {\n')
            html.write('  color: #6495ED;\n')
            html.write('}\n\n')
            html.write('</style>\n\n')
            html.write('</head>\n\n')
            html.write('<body>\n')
            html.write('<script type="text/javascript" language="JavaScript1.2">\n\n')
            html.write('var planets = new Array();\n\n')
            #phew thats a lot of writing to a file

            scan=open(name,'r')

            for line1 in scan:
                nend=line1.find(']')
                pname=line1[7:nend]
                if pname.find("'")!=-1:
                    pname=pname.replace("'","")
                if line1.find('Gravity')!=-1:            
                    (grav,temp,atmos,suit)=moresuitstuff(line1)
                    towrite="planets['%s'] = '%s %s %s --  %s%%';\n" % (pname,\
                                                                        grav,\
                                                                        temp,\
                                                                        atmos,\
                                                                        suit)
                    html.write(towrite)
            html.write('\n')
            html.write('function myTipHide()\n')
            html.write('{\n')
            html.write("    document.getElementById('tooltip').style.display="\
                       "'none';\n")
            html.write('}\n\n')
            html.write('function myTip(thing)\n')
            html.write('{\n')
            html.write('    var off=document.getElementById(thing);\n\n')
            html.write('    if (off.offsetParent) {\n')
            html.write('        var curleft = 0;\n')
            html.write('        var curtop = 0;\n')
            html.write('        while (off) {\n')
            html.write('            curleft += off.offsetLeft;\n')
            html.write('            curtop += off.offsetTop;\n')
            html.write('            off=off.offsetParent;\n')
            html.write('        }\n')
            html.write('    }\n\n')
            html.write("    document.getElementById('tooltip').style.top   = "\
                       "curtop+15+'px';\n")
            html.write("    document.getElementById('tooltip').style.left  = "\
                       "curleft+'px';\n\n")
            html.write("    divtitle = document.getElementById('tooltiphead');\n")
            html.write('    divtitle.innerHTML = planets[thing];\n\n')
            html.write("    thediv = document.getElementById('tooltip');\n")
            html.write("    if(thediv.style.display != 'block' ){\n")
            html.write("        thediv.style.display = 'block'\n")
            html.write('    }else{\n')
            html.write("        thediv.style.display = 'none'\n")
            html.write('    }\n')
            html.write('}\n\n')
            html.write('function myAmountTipHide()\n')
            html.write('{\n')
            html.write("    document.getElementById('amounttip').style.display="\
                       "'none';\n")
            html.write('}\n\n')
            html.write('function myAmountTip(thing,text)\n')
            html.write('{\n')
            html.write('    var off=document.getElementById(thing);\n\n')
            html.write('    if (off.offsetParent) {\n')
            html.write('        var curleft = 0;\n')
            html.write('        var curtop = 0;\n')
            html.write('        while (off) {\n')
            html.write('             curleft += off.offsetLeft;\n')
            html.write('             curtop += off.offsetTop;\n')
            html.write('             off=off.offsetParent;\n')
            html.write('        }\n')
            html.write('    }\n\n')
            html.write("    document.getElementById('amounttip').style.top   = "\
                       "curtop+15+'px';\n")
            html.write("    document.getElementById('amounttip').style.left  = "\
                       "curleft+'px';\n\n")
            html.write("    thediv = document.getElementById('amounttip');\n")
            html.write('    thediv.innerHTML = text;\n')
            html.write("    if(thediv.style.display != 'block' ){\n")
            html.write("         thediv.style.display = 'block'\n")
            html.write('    }else{\n')
            html.write("        thediv.style.display = 'none'\n")
            html.write('    }\n')
            html.write('}\n\n')
            html.write('function myHLOn(name)\n')
            html.write('{\n')
            html.write('    var e=document.getElementsByName(name);\n')
            html.write("    for(var i=0;i<e.length;i++){e[i].style.textDecoration  = "\
                       "'underline';}\n")
            html.write('}\n\n')
            html.write('function myHLOff(name)\n')
            html.write('{\n')
            html.write('    var e=document.getElementsByName(name);\n')
            html.write("    for(var i=0;i<e.length;i++){e[i].style.textDecoration  = "\
                       "'none';}\n")
            html.write('}\n\n\n')
            html.write('</script>\n\n')
            #phew, too much style!

            h1='<h1>%s</h1>\n\n' % name[:-4]
            html.write(h1)
            html.write('<table cellpadding=3 cellspacing=0 border=0>')
            #complicated coming up

            scan.seek(0)
            
            planet=0
            amount_counter=0
            for line in scan:
                if line.find('Gravity')!=-1:
                    planet+=1
                    (grav, temp,atmos,suit)=moresuitstuff(line)
                    ssuit=suitshort(line)
                    nend=line.find(']')
                    pname=line[7:nend]
                    if pname.find("'")!=-1:
                        pname=pname.replace("'","")
                    if planet>1:
                        html.write('<tr><td>&nbsp;</td></tr>\n')
                    fwrite="""<tr class="p"><td colspan=2><br>P: [%s]</td><td><br>"""\
                            """<div style="width: 10px; white-space: nowrap;" id='%s' """\
                            """class='suit' onMouseOver="myTip('%s');" onMouseOut="""\
                            """"myTipHide();">%s %s%%</div></td></tr>\n""" % (pname,\
                                                                              pname,\
                                                                              pname,\
                                                                              ssuit,\
                                                                              suit)
                    html.write(fwrite)

                    dot=line.find('.')
                    commods=line[dot+2:len(line)-1]
                    if commods.find('Colony')!=-1:
                        commods=commods[23:]
                        sp=commods.find(' ')+1
                        commods=commods[sp:]
                    clist=commods.split(', ')
                    html.write('<tr>\n')
                    html.write('    <td>&nbsp;</td>\n')
                    html.write('    <td colspan=2>\n')
                    for m in range(len(clist)):
                        if clist[m].find('Ruins')==-1:
                            amount_counter+=1
                            (amount, com)=commods_parse(clist[m])
                            numam=num_amount(amount)
                            col=color(com)
                            forwriting="""        <span class='a' id='amount%s' """\
                                        """onMouseOver="myAmountTip('amount%s','%s');" """\
                                        """onMouseOut="myAmountTipHide();">%s</span>""" \
                                        % (amount_counter,amount_counter,numam,amount)
                            forwriting2="<span style='color: %s;' >%s</span>" % (col,com)
                            if len(clist)-(m+1)!=0:
                                forwriting3=',\n'
                            else:
                                forwriting3='\n'
                            html.write(forwriting+forwriting2+forwriting3)
                        elif clist[m].find('Ruins')!=-1:
                            ruinwrite="        <span style='color: #A0522D'>%s</span>" % clist[m]
                            if len(clist)-(m+1)!=0:
                                ruinwrite+=',\n'
                            else:
                                ruinwrite+='\n'
                            html.write(ruinwrite)
                        else:
                            pass
                    html.write('    </td>\n')
                    html.write('</tr>\n')
                    #end of planet writing

                    
                elif line.find('Gravity')==-1:
                    nend=line.find(']')
                    mname=line[7:nend]
                    if mname.find("'")!=-1:
                        mname=mname.replace("'","")
                    mwrite="<tr><td>&nbsp;</td><td class='m'>M: [%s]</td>\n" % mname
                    html.write(mwrite)
                    html.write("<td class='m2'>\n")
                    
                    commods=line[nend+2:len(line)-1]
                    clist=commods.split(', ')
                    for nn in range(len(clist)):
                        amount_counter+=1
                        if clist[nn].find('Ruins')==-1:
                            (amount, com)=commods_parse(clist[nn])
                            numam=num_amount(amount)
                            col=color(com)
                            forwriting="""        <span class='a' id='amount%s' onMouseOver="""\
                                        """"myAmountTip('amount%s','%s');" onMouseOut="myAmountTipHide()"""\
                                        """;">%s</span>""" % (amount_counter,amount_counter,numam,amount)
                            forwriting2="<span style='color: %s;' >%s</span>" % (col,com)
                            if len(clist)-(nn+1)!=0:
                                forwriting3=',\n'
                            else:
                                forwriting3='\n'
                            html.write(forwriting+forwriting2+forwriting3)
                        else:
                            pass
                    html.write('    </td>\n')
                    html.write('</tr>\n')
                # End of scanning through the scan file!
                
            html.write('</table>\n')
            html.write('<br><br>\n\n')

            for name in scanlist:
                hname=name[:-4]+'.html'
                if name==scanlist[n]:
                    html.write(name[:-3]+'<br>')
                else:
                    etirw='<a href="%s">%s</a><br>\n' % (hname,name[:-3])
                    html.write(etirw)

            html.write('\n\n')
            html.write('<div id="tooltip" class="xstooltip"><div id="tooltiphead" '\
                       'class="xstooltiphead"></div></div>\n')
            html.write('<div id="amounttip" class="xsamounttip"></div>\n')
            html.write('</body>\n')
            html.write('</html>')

            html.close()
            scan.close()

                
            

if __name__=="__main__":
    app=UberScanner(None)
    app.title('Uber Scanner')
    app.iconbitmap('uberscanner.ico')
    app.resizable(0,0)
    #app.configure(bg='blue')
    app.mainloop()
