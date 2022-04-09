import os
import configparser

def main(tf_dir='C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf', conf='config.ini', configpathway=True):
    cfg_dir = tf_dir + '/cfg'
    if configpathway == True:
        config = configparser.ConfigParser()
        if os.path.exists(conf):
            config.read(conf)

            defaultbinds = ['', '', '', '', '', '', '', '', '', '']
            defaultbinds[0] = config['DEFAULTBINDS']['key1']
            defaultbinds[1] = config['DEFAULTBINDS']['key2']
            defaultbinds[2] = config['DEFAULTBINDS']['key3']
            defaultbinds[3] = config['DEFAULTBINDS']['key4']
            defaultbinds[4] = config['DEFAULTBINDS']['key5']
            defaultbinds[5] = config['DEFAULTBINDS']['key6']
            defaultbinds[6] = config['DEFAULTBINDS']['key7']
            defaultbinds[7] = config['DEFAULTBINDS']['key8']
            defaultbinds[8] = config['DEFAULTBINDS']['key9']
            defaultbinds[9] = config['DEFAULTBINDS']['key0']

            binds = ['', '', '', '', '', '', '']
            binds[0] = config['BINDS']['key1']
            binds[1] = config['BINDS']['key2']
            binds[2] = config['BINDS']['key3']
            binds[3] = config['BINDS']['key4']
            binds[4] = config['BINDS']['key5']
            binds[5] = config['BINDS']['key6']
            binds[6] = config['BINDS']['key7']
            
            tf_dir = config['CONFIG']['tf_dir']
            prefix = config['CONFIG']['prefix']
            folder = config['CONFIG']['folder']
            number = config['CONFIG']['number']
            is_lastpage = config['CONFIG']['is_lastpage']
        else:
            config['CONFIG'] = {}
            config['CONFIG']['tf_dir'] = 'C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf'
            config['CONFIG']['prefix'] = 'none'
            config['CONFIG']['folder'] = 'none'
            config['CONFIG']['number'] = '1'
            config['CONFIG']['is_lastpage'] = 'false'

            defaultbinds = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7', 'slot8', 'slot9', 'slot10']
            config['DEFAULTBINDS'] = {}
            config['DEFAULTBINDS']['key1'] = defaultbinds[0]
            config['DEFAULTBINDS']['key2'] = defaultbinds[1]
            config['DEFAULTBINDS']['key3'] = defaultbinds[2]
            config['DEFAULTBINDS']['key4'] = defaultbinds[3]
            config['DEFAULTBINDS']['key5'] = defaultbinds[4]
            config['DEFAULTBINDS']['key6'] = defaultbinds[5]
            config['DEFAULTBINDS']['key7'] = defaultbinds[6]
            config['DEFAULTBINDS']['key8'] = defaultbinds[7]
            config['DEFAULTBINDS']['key9'] = defaultbinds[8]
            config['DEFAULTBINDS']['key0'] = defaultbinds[9]

            binds = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7']
            config['BINDS'] = {}
            config['BINDS']['key1'] = binds[0]
            config['BINDS']['key2'] = binds[1]
            config['BINDS']['key3'] = binds[2]
            config['BINDS']['key4'] = binds[3]
            config['BINDS']['key5'] = binds[4]
            config['BINDS']['key6'] = binds[5]
            config['BINDS']['key7'] = binds[6]
            with open(conf, 'w') as configfile:
                config.write(configfile)
            return None
    else:
        prefix = conf['CONFIG']['prefix']
        folder = conf['CONFIG']['folder']
        number = conf['CONFIG']['number']
        is_lastpage = conf['CONFIG']['is_lastpage']

        defaultbinds = ['', '', '', '', '', '', '', '', '', '']
        defaultbinds[0] = conf['DEFAULTBINDS']['key1']
        defaultbinds[1] = conf['DEFAULTBINDS']['key2']
        defaultbinds[2] = conf['DEFAULTBINDS']['key3']
        defaultbinds[3] = conf['DEFAULTBINDS']['key4']
        defaultbinds[4] = conf['DEFAULTBINDS']['key5']
        defaultbinds[5] = conf['DEFAULTBINDS']['key6']
        defaultbinds[6] = conf['DEFAULTBINDS']['key7']
        defaultbinds[7] = conf['DEFAULTBINDS']['key8']
        defaultbinds[8] = conf['DEFAULTBINDS']['key9']
        defaultbinds[9] = conf['DEFAULTBINDS']['key0']

        binds = ['', '', '', '', '', '', '']
        binds[0] = conf['BINDS']['key1']
        binds[1] = conf['BINDS']['key2']
        binds[2] = conf['BINDS']['key3']
        binds[3] = conf['BINDS']['key4']
        binds[4] = conf['BINDS']['key5']
        binds[5] = conf['BINDS']['key6']
        binds[6] = conf['BINDS']['key7']

    if not os.path.exists(os.path.join(cfg_dir)):
        os.mkdir(cfg_dir)
    if not os.path.exists(os.path.join(f'{cfg_dir}/{folder}')):
        os.mkdir(f'{cfg_dir}/{folder}')
    with open(os.path.join(f'{cfg_dir}/{folder}', f'{prefix}_page{number}.cfg'), 'w+') as f:
        previouspage_bind = f'bind 8 {prefix}_previouspage'
        nextpage_bind = f'bind 9 {prefix}_nextpage'
        close_bind = f'bind 0 {prefix}_restore_binds'
        close_button = f'alias {prefix}_restore_binds \"bind 1 {defaultbinds[0]}; bind 2 {defaultbinds[1]}; bind 3 {defaultbinds[2]}; bind 4 {defaultbinds[3]}; bind 5 {defaultbinds[4]}; bind 6 {defaultbinds[5]}; bind 7 {defaultbinds[6]}; bind 8 {defaultbinds[7]}; bind 9 {defaultbinds[8]}; bind 0 {defaultbinds[9]}; \"'
        if number == '1':
            previouspage = 'echo you are at the first page.'
        else:
            previouspage = f'exec {folder}/{prefix}_page{int(number)-1}; echo current page: {int(number)-1}'

        if is_lastpage.lower() == 'true':
            nextpage = 'echo you are at the last page.'
        elif is_lastpage.lower() == 'false':
            nextpage = f'echo current page: {int(number)+1}; exec {folder}/{prefix}_page{int(number)+1}'

        f.write(f'''alias {prefix}_previouspage "{previouspage}"
alias {prefix}_nextpage "{nextpage}"
alias {prefix}_currentpage "exec {folder}\{prefix}_visual_menu{number}; echo current page: {number}"
{prefix}_currentpage
{close_button}
{close_bind}
{previouspage_bind}
{nextpage_bind}

exec "{folder}\{prefix}_page{number}_binds"''')
    with open(os.path.join(f'{cfg_dir}/{folder}', f'{prefix}_page{number}_binds.cfg'), 'w') as f:
        f.write(f'''bind 1 "{binds[0]}"
bind 2 "{binds[1]}"
bind 3 "{binds[2]}"
bind 4 "{binds[3]}"
bind 5 "{binds[4]}"
bind 6 "{binds[5]}"
bind 7 "{binds[6]}"''')
        with open(os.path.join(f'{cfg_dir}/{folder}', f'{prefix}_visual_menu{number}.cfg'), 'w+') as f:
            f.write('echo')
            f.write('echo \"' + str(binds[0]) + '\"\n')
            f.write('echo \"' + str(binds[1]) + '\"\n')
            f.write('echo \"' + str(binds[2]) + '\"\n')
            f.write('echo \"' + str(binds[3]) + '\"\n')
            f.write('echo \"' + str(binds[4]) + '\"\n')
            f.write('echo \"' + str(binds[5]) + '\"\n')
            f.write('echo \"' + str(binds[6]) + '\"')
