import os
import configparser

cfg = configparser.ConfigParser()
if os.path.exists('config.ini'):
    cfg.read('config.ini')
    prefix = cfg['CONFIG']['prefix']
else:
    prefix = 'None'

def main(cfg_dir, folder, prefix=None):
    if cfg_dir[-3:] != 'cfg':
        cfg_dir += '/cfg' 
    os.chdir(cfg_dir)
    onlyfiles = [yy for yy in os.listdir(folder) if os.path.isfile(os.path.join(folder, yy))]
    if prefix is None:
        prefix = onlyfiles[2].partition('_')[0]
    x = os.path.basename(folder)
    if folder != '':
        y = 0
        if os.path.exists(folder):
            while y != 35:
                y += 1
                try:
                    with open(os.path.join(folder, f'{prefix}_page{y}_binds.cfg'), 'r') as f:
                        content = f.readlines()
                        content = [x.strip() for x in content]
                        content[0] = content[0][7:]
                        content[1] = content[1][7:]
                        content[2] = content[2][7:]
                        content[3] = content[3][7:]
                        content[4] = content[4][7:]
                        content[5] = content[5][7:]
                        content[6] = content[6][7:]
                    with open(os.path.join(folder, f'{prefix}_visual_menu{y}.cfg'), 'w+') as f:
                        f.write('echo [' + str(content[0]) + ']\n')
                        f.write('echo [' + str(content[1]) + ']\n')
                        f.write('echo [' + str(content[2]) + ']\n')
                        f.write('echo [' + str(content[3]) + ']\n')
                        f.write('echo [' + str(content[4]) + ']\n')
                        f.write('echo [' + str(content[5]) + ']\n')
                        f.write('echo [' + str(content[6]) + ']')
                except:
                    break