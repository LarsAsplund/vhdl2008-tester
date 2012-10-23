#!/usr/bin/python

import os
import subprocess

class Compiler:
    def compile(self, filename):
        return False
        
class VcomCompiler(Compiler):
    arguments = ["-2008"]
    def __init__(self):
        self.vlib = self.installationDir + "vlib"
        self.vcom = self.installationDir + "vcom"
        subprocess.Popen([self.vlib] + ["work"])
    def compile (self,filename):
        #exitCode = os.spawnv(os.P_WAIT, self.vcom, self.arguments + [filename])
        p = subprocess.Popen([self.vcom] + self.arguments + [filename],stdout=subprocess.PIPE)
        process_output = p.communicate()[0]
        for line in process_output.split('\n'):
            if line.startswith(self.errorCode):
                return False
        return True
        
class RivieraCompiler (VcomCompiler):
    installationDir = "/Users/philippe.faes/Dropbox/fakeRiviera/"
    errorCode = "COMP96 Compile failure"

class ModelsimCompiler (VcomCompiler):
    installationDir = "/Users/philippe.faes/Dropbox/fakeVsim/"
    errorCode = "** Error"

allDirNames = ['smoketest/',
               # 'reserved_names/',
               'vhdl2008/']
allFileNamess = [[dirname+filename for filename in os.listdir(dirname)] for dirname in allDirNames]
allFileNames = reduce( lambda x,y : x+y , allFileNamess, [])
fileNames =  [filename for filename in allFileNames if filename.endswith(".vhd")]
#fileNames = ["smoketest/t0.vhd","smoketest/t1.vhd"]

riviera = RivieraCompiler()
modelsim = ModelsimCompiler()

results={}
for filename in fileNames:
    f = file (filename)
    lines = f.readline()
    f.close;
    results[filename] = [lines, modelsim.compile(filename) , riviera.compile(filename)]

def mark(value):
    return "-+"[value]

for filename in fileNames:
    r=results[filename]
    print r[0][0:-1] + ("_"*(50-len(r[0]))) + " " + mark(r[1]) + " " + mark(r[2])
