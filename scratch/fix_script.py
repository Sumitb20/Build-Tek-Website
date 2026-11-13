import os

def fix_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix line 1412: var nToggle=,mNav=;
    content = content.replace(
        'var nToggle=,mNav=;\nif(nToggle&&mNav){\n  nToggle.addEventListener(\'click\',function(){mNav.classList.toggle(\'open\');nToggle.classList.toggle(\'active\')});\n  mNav.querySelectorAll(\'a\').forEach(function(l){l.addEventListener(\'click\',function(){mNav.classList.remove(\'open\');nToggle.classList.remove(\'active\')})});\n}',
        'var nToggle = document.getElementById("navToggle"), mNav = document.querySelector(".bar nav");\nif (nToggle && mNav) {\n  nToggle.addEventListener("click", function() {\n    mNav.classList.toggle("open");\n    nToggle.classList.toggle("active");\n  });\n  mNav.querySelectorAll("a").forEach(function(l) {\n    l.addEventListener("click", function() {\n      mNav.classList.remove("open");\n      nToggle.classList.remove("active");\n    });\n  });\n}'
    )

    # 2. Fix line 1433: if(reduce){$('#loader').style.display='none';ready();return}
    # On mobile, skip the 5s preloader so the site shows immediately!
    content = content.replace(
        "if(reduce){$('#loader').style.display='none';ready();return}",
        '''var isMobileInit = (window.innerWidth <= 960) || ('ontouchstart' in window);
if (reduce || isMobileInit) {
  var ldr = document.getElementById('loader');
  if (ldr) ldr.style.display = 'none';
  var wp = document.getElementById('wipe');
  if (wp) wp.style.display = 'none';
  document.body.classList.remove('lock');
  ready();
  return;
}'''
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed {file_path}")

fix_file('/home/sumit/.gemini/antigravity-ide/scratch/BuildTek-Website/index.html')
fix_file('/home/sumit/Downloads/Others/Build Tek Events.html')
