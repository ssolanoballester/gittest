#!/usr/bin/env python

#import sys
import os, re

print "Triliriiii..."

#Cadena="mi cadena"

#if Cadena.islower():
#    print "cadena en minusculas"
#else:
#    print "Cadena en no minusculas"

linea="/app/apache/tomcat/jdk/1.8.0_112/bin/java -Djava.util.logging.config.file=/data/apache/tomcat/rad/instances/RADSTT00/conf/logging.properties -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager -server -Xms256m -Xmx256m -XX:PermSize=128m -Dname=RADSTT00 -Dorg.apache.catalina.connector.CoyoteAdapter.ALLOW_BACKSLASH=false -Dorg.apache.tomcat.util.buf.UDecoder.ALLOW_ENCODED_SLASH=false -Dorg.apache.catalina.connector.RECYCLE_FACADES=true -verbose:gc -XX:+PrintGCDetails -Xloggc:/data/apache/tomcat/rad/instances/RADSTT00/logs/gc-RADSTT00.log -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=/data/apache/tomcat/rad/instances/RADSTT00/logs/OOM_dumps -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9001 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=true -Dcom.sun.management.jmxremote.password.file=/data/apache/tomcat/rad/instances/RADSTT00/conf/jmx.pass -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000 -Djdk.tls.ephemeralDHKeySize=2048 -Djava.protocol.handler.pkgs=org.apache.catalina.webresources -Djava.endorsed.dirs=/app/apache/tomcat/8.0.38/endorsed -classpath /app/apache/tomcat/8.0.38/bin/bootstrap.jar:/app/apache/tomcat/8.0.38/bin/tomcat-juli.jar -Dcatalina.base=/data/apache/tomcat/rad/instances/RADSTT00 -Dcatalina.home=/app/apache/tomcat/8.0.38 -Djava.io.tmpdir=/data/apache/tomcat/rad/instances/RADSTT00/temp org.apache.catalina.startup.Bootstrap start"

#print linea


#if re.search(r'org\.apache\.catalina\.startup\.Bootstrap\sstart',linea):
#if re.search(r'[w.-]+org\.apache\.catalina\.startup\.Bootstrap\sstart[w.-]+', linea):
if re.search(r'org\.apache\.catalina\.startup\.Bootstrap\sstart', linea):
    print "cadena encontrada"
#if cadena2:



print"\n\n\n===============================================================\n"

#Get process list
pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

#print((os.getcwd()))

#print(pids)

instancias=[]

#cadena=u"org.apache.catalina.startup.Bootstrap\ start"
cadena="org.apache.catalina.startup.Bootstrap start"

#cadena2=re.search(r'org\.apache\.catalina\.startup\.Bootstrap\sstart',cadena)
#if cadena2:
#    print "cadena encontrada"

#print("el tipo de cadena2 es:")
#print(type(cadena2))
#print(cadena2)

proceso=""

#Go through process list
for pid in pids:
    try:
        #print open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
        perraco=open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
        #print (type(perraco))
        #print perraco
        #if perraco.__contains__("org.apache.catalina.startup.Bootstrap" + " " + "start"):
        #if perraco.__contains__("org.apache.catalina.startup.Bootstrap start"):
        #if perraco.__contains__(cadena):
        #if perraco.find("org.apache.catalina.startup.Bootstrap") == -1:
        #if perraco.find(cadena) == -1:
        #    pass
        #if encontrado=re.search(r'[\w.-]org\.apache\.catalina\.startup\.Bootstrap\sstart[\w.-]]',perraco):
        #encontrado=re.search(r'[\w.-]org\.apache\.catalina\.startup\.Bootstrap\sstart[\w.-]',perraco)
        #encontrado = re.search(r'org\.apache\.catalina\.startup\.Bootstrap\sstart', perraco)
        #if re.search(r'[w.-]+org\.apache\.catalina\.startup\.Bootstrap\sstart[w.-]', linea):
        #if re.search(r'org\.apache\.catalina\.startup\.Bootstrap\sstart', linea): FUNCIONA!!!
        #if re.search(r'org\.apache\.catalina\.startup\.Bootstrap\sstart\s', perraco):
        #if re.search(r'org\.apache\.catalina\.startup\.Bootstrap', perraco): # FUNCIONA!!!
        if re.search(r'org\.apache\.catalina\.startup\.Bootstrap\Sstart', perraco):
            print perraco
            #print encontrado
            #proceso=perraco
            #print proceso
            #print perraco
        #else:
            #print "Yes It's here"
            #print perraco
        #if "org.apache.catalina.startup.Bootstrap " in perraco.__contains__("org.apache.catalina.startup.Bootstrap start"):
            #instancias.append(perraco)
    except IOError: #proc has already terminated
        continue

#print (type(perraco))
#print (perraco)
#print(instancias)
#print (proceso)



#TO-DO List
# - Ver que maneras hay de localizar una subcadena dentro de una cadena (para ver la cadena del proceso).
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -