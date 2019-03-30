import site,os,sys
import shutil
syspath=os.environ['path']

def folder_walk(folder):
    for root, dirs, files in os.walk(folder):
        return [os.path.join(folder,name) for name in files]
def write_init(path):
    file1=open(path,'w')
    file1.write("__version__ = '1.0.7'")
    file1.close()
def getsitepackpath():
    sitepackagepath=''
    for s in site.getsitepackages():
        if s.endswith('site-packages'):
            sitepackagepath = s
            for p in [os.path.abspath(p) for p in syspath.split(';')]:
                if os.path.abspath(p).lower()==os.path.abspath(s).lower():
                    return sitepackagepath
    return    
def setup_package():
    sitepackagepath = getsitepackpath()
    if not sitepackagepath:
        print "Please set python sitepackage path first!"
        return
    extend_folder = os.path.join(sitepackagepath,'extend')
    try:
        os.mkdir(extend_folder)
    except Exception as e:
        print e
    local_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'EXTEND')
    files=folder_walk(local_path)
    write_init(os.path.join(extend_folder,'__init__.py'))
    for f in files:
        shutil.copy(f,os.path.join(extend_folder,os.path.basename(f)))


if __name__ == '__main__':
    local_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    setup_package()