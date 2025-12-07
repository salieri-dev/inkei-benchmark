- [common\_0.js](#common_0js)
- [main\_u3d.js](#main_u3djs)
- [orig\_inkei.css](#orig_inkeicss)
- [orig\_inkei.js](#orig_inkeijs)
- [Penis of A - Penis Analyzer.html](#penis-of-a---penis-analyzerhtml)

---

## common_0.js
**Path:** `common_0.js`

```javascript
var clsClass=clsClass||{};clsClass.fnCopyClass=function(a){if(null==a||"object"!=typeof a)return a;var b=a.constructor(),c;for(c in a)a.hasOwnProperty(c)&&(b[c]=a[c]);return b};var clsPanel=clsPanel||{};
clsPanel={elmPn:null,actxCv:null,iW:0,iH:0,iPer:0,sbInit:function(a,b,c,d,e,f){f=clsPanel.fnGetWindowWidth(f,c,e);c=Math.floor(d/c*f);iPer=f/e;clsPanel.iW=f;clsPanel.iH=c;clsPanel.iPer=iPer;clsPanel.elmPn=document.getElementById(a);clsPanel.elmPn.style.width=f+"px";clsPanel.elmPn.style.height=c+"px";if(""!=b)for(a=b.split(","),clsPanel.actxCv={},b=0,e=a.length;b<e;b++){d=a[b];var g=document.getElementById(d);g.setAttribute("width",f);g.setAttribute("height",c);clsPanel.actxCv[d]=g.getContext("2d")}},
sbInitConstBase:function(a,b,c,d,e){clsPanel.iW=c;clsPanel.iH=d;clsPanel.iPer=e;b=b.split(",");clsPanel.elmPn=document.getElementById(a);clsPanel.elmPn.style.width=c+"px";clsPanel.elmPn.style.height=d+"px";clsPanel.actxCv={};a=0;for(e=b.length;a<e;a++){var f=b[a],g=document.getElementById(f);g.setAttribute("width",c);g.setAttribute("height",d);clsPanel.actxCv[f]=g.getContext("2d")}},sbInitHeightBase:function(a,b,c,d,e,f,g){c=clsPanel.fnGetWindowWidth(f,c,e)*g;f=clsPanel.fnGetWindowHeight(f);iH=c<
f?c:f;iW=iH/g;iPer=iW/e;clsPanel.iW=iW;clsPanel.iH=iH;clsPanel.iPer=iPer;b=b.split(",");clsPanel.elmPn=document.getElementById(a);clsPanel.elmPn.style.width=iW+"px";clsPanel.elmPn.style.height=iH+"px";clsPanel.actxCv={};a=0;for(e=b.length;a<e;a++)g=b[a],f=document.getElementById(g),f.setAttribute("width",iW),f.setAttribute("height",iH),clsPanel.actxCv[g]=f.getContext("2d")},fnGetWindowWidth:function(a,b,c){if(window.innerWidth)var d=window.innerWidth;else document.documentElement&&0!=document.documentElement.clientWidth?
d=document.documentElement.clientWidth:document.body&&(d=document.body.clientWidth);d-=2*a;d=d<b?b:d;return d>c?c:d},fnGetWindowHeight:function(a){if(window.innerHeight)var b=window.innerHeight;else document.documentElement&&0!=document.documentElement.clientHeight?b=document.documentElement.clientHeight:document.body&&(b=document.body.clientHeight);return b-2*a},sbClearPanel:function(){},fnGetTableText:function(a,b,c,d,e,f,g,l,k,h){k=k||"";k=""==k?"":" "+k;h=h||"";h=""==h?"":" "+h;g.match(/^[0-9a-fA-F]{6}$/g)&&
(g="#"+g);a=Math.ceil(a);b=Math.ceil(b);c=Math.floor(c);d=Math.floor(d);f=Math.ceil(f);c=1<c?c:1;var n="";0<=a&&0<=b&&a+c<=clsPanel.iW&&b+d<=clsPanel.iH&&(n+='<table style="left:'+a+"px; top:"+b+"px; width:"+c+"px;height:"+d+"px;"+k+'"'+h+'><tr><td style="font-size:'+f+"px; color:"+g+"; text-align:"+("c"==e?"center":"r"==e?"right":"left")+';">'+l+"</td></tr></table>");return n}};var clsParam=clsParam||{};
clsParam={dMain:null,strId:"",iInputCount:0,sbInit:function(a,b){clsParam.dMain=a;clsParam.strId=b;for(var c=0;100>c&&clsParam.dMain.getElementById(clsParam.strId+c);c++);clsParam.iInputCount=c},sbGetParam:function(){var a=clsParam.dMain.location.search.substring(1).split("&");for(var b=0,c=a.length;b<c;b++){var d=a[b].indexOf("=");0<d&&(strKey=a[b].substring(0,d),strVal=a[b].substring(d+1),a[strKey]=strVal)}return a},sbParam2Form:function(a,b,c,d,e){void 0===a&&(a="");void 0===b&&(b=0);void 0===
c&&(c=!0);void 0===d&&(d="");void 0===e&&(e="");"group"==d&&(c=!0);var f=clsParam.sbGetParam();var g="";""!=a&&a in f&&(g=f[a]);""==g&&(a=(""+clsParam.dMain.location).split("/"),g=a[a.length-1]);1==b&&(g=clsParam.fnDecryptionURI(g));g=decodeURI(g);g=g.replace(/#.*/,"");if(""!=g)if(g=g.replace(/[,;!]/g,"\n"),c&&(g=g.replace(/\n+/g,"\n"),g=g.replace(/^\n+/g,""),g=g.replace(/\n+$/g,"")),b=g.split("\n"),"simple"==d)for(a=Number(e),d=0;d<clsParam.iInputCount&&d<b.length;d++)e=b[d],e=e.replace(/_/g," "),
clsParam.fnIsYYYYMMDD(e)&&(d=a),c=clsParam.dMain.getElementById(clsParam.strId+d),c.value=e;else if("group"==d)for(a=e,f="",0<b.length&&(f=b[b.length-1]),d=g=0;d<clsParam.iInputCount;d++)c=clsParam.dMain.getElementById(clsParam.strId+d),a.substr(d,1)==f.substr(g,1)&&(e=b[g],e=e.replace(/_/g," "),c.value=e,g++);else for(d=0;d<clsParam.iInputCount&&d<b.length;d++)c=clsParam.dMain.getElementById(clsParam.strId+d),e=b[d],e=e.replace(/_/g," "),c.value=e},fnIsYYYYMMDD:function(a){if(!a.match(/^\d{4}\d{2}\d{2}$/))return!1;
var b=a.substr(0,4)-0,c=a.substr(4,2)-1;a=a.substr(6,2)-0;var d=new Date(b,c,a);return isNaN(d)?!1:d.getFullYear()==b&&d.getMonth()==c&&d.getDate()==a?!0:!1},sbSendForm:function(a,b,c,d){void 0===a&&(a="");void 0===b&&(b=0);void 0===c&&(c=!0);void 0===d&&(d="");""!=d&&(c=!0);var e=""+clsParam.dMain.location;e=e.replace(/^(.*\/).*$/,"$1");e=e.split("?")[0];for(var f,g="",l="",k=0;k<clsParam.iInputCount;k++)if(f=clsParam.dMain.getElementById(clsParam.strId+k))f=f.value,f=f.replace(/[,;!<>\/\^\?]/g,
""),c?""!=f&&(g+=(""==g?"":"!")+f,""!=d&&(l+=d.substr(k,1))):g+=(0==k?"":"!")+f;else break;c&&(g=g.replace(/!+/g,"!").replace(/^!+/g,"").replace(/!+$/g,""));g=g.replace(/ /g,"_");""!=l&&(g+="!"+l);c=""+e;""!=g&&(g=encodeURI(g),1==b&&(g=clsParam.fnEncryptionURI(g)),clsParam.dMain.location=c+(""+a+g));return!1},fnGetParamText:function(a,b){void 0===a&&(a="");void 0===b&&(b=0);var c=clsParam.sbGetParam();var d="";""!=a&&a in c&&(d=c[a]);""==d&&(c=(""+clsParam.dMain.location).split("/"),d=c[c.length-
1]);1==b&&(d=clsParam.fnDecryptionURI(d));return d=decodeURI(d)},sbSendText:function(a,b,c){void 0===b&&(b="");void 0===c&&(c=0);var d=""+clsParam.dMain.location;d=d.replace(/^(.*\/).*$/,"$1");d=d.split("?")[0];d=""+d;""!=a&&(a=encodeURI(a),1==c&&(a=clsParam.fnEncryptionURI(a)),clsParam.dMain.location=d+(""+b+a));return!1},fnEncryptionURI:function(a){a=a.replace(/~/g,"");for(var b="",c=0,d=a.length;c<d;c++){var e=a.charCodeAt(c);b+=String.fromCharCode(48<=e&&57>=e?(e-48+1)%10+48:97<=e&&102>=e?(e-
97+1)%6+97:103<=e&&122>=e?(e-103+1)%20+103:65<=e&&70>=e?(e-65+1)%6+65:71<=e&&90>=e?(e-71+1)%20+71:37==e?126:126==e?37:e)}return b=encodeURI(b)},fnDecryptionURI:function(a){a=decodeURI(a);for(var b="",c=0,d=a.length;c<d;c++){var e=a.charCodeAt(c);b+=String.fromCharCode(48<=e&&57>=e?(e-48+9)%10+48:97<=e&&102>=e?(e-97+5)%6+97:103<=e&&122>=e?(e-103+19)%20+103:65<=e&&70>=e?(e-65+5)%6+65:71<=e&&90>=e?(e-71+19)%20+71:37==e?126:126==e?37:e)}return b}};var clsDragdealer=clsDragdealer||{};
clsDragdealer={atxtMain:null,addMain:null,aiMin:null,aiMax:null,aiStep:null,sbInit:function(a,b,c,d,e,f){clsDragdealer.atxtMain||(clsDragdealer.atxtMain=[]);clsDragdealer.atxtMain[a]=document.getElementById(b);clsDragdealer.addMain||(clsDragdealer.addMain=[]);clsDragdealer.addMain[a]=c;clsDragdealer.aiMin||(clsDragdealer.aiMin=[]);clsDragdealer.aiMin[a]=d;clsDragdealer.aiMax||(clsDragdealer.aiMax=[]);clsDragdealer.aiMax[a]=e;clsDragdealer.aiStep||(clsDragdealer.aiStep=[]);clsDragdealer.aiStep[a]=
f},sbSlide:function(a,b){clsDragdealer.sbSetValueText(a,clsDragdealer.aiMin[a]+(clsDragdealer.aiMax[a]-clsDragdealer.aiMin[a])*b)},sbInput:function(a){var b=clsDragdealer.atxtMain[a].value,c=clsDragdealer.aiMin[a];b.match(/[^0-9|^\-|^\.]/g)||(c=Number(b));c<clsDragdealer.aiMin[a]&&(c=clsDragdealer.aiMin[a]);c>clsDragdealer.aiMax[a]&&(c=clsDragdealer.aiMax[a]);clsDragdealer.sbSetValue(a,c)},sbSetValue:function(a,b){clsDragdealer.sbSetValueDd(a,b);clsDragdealer.sbSetValueText(a,b)},sbSetValueDd:function(a,
b){b=clsDragdealer.fnAdjustValue(a,b);clsDragdealer.addMain[a].setValue((b-clsDragdealer.aiMin[a])/(clsDragdealer.aiMax[a]-clsDragdealer.aiMin[a]))},sbInitXY:function(a,b,c,d,e,f,g,l,k,h,n,p){clsDragdealer.addMain||(clsDragdealer.addMain=[]);clsDragdealer.addMain[a]=b;clsDragdealer.atxtMain||(clsDragdealer.atxtMain=[]);clsDragdealer.atxtMain[c]=document.getElementById(d);clsDragdealer.atxtMain[l]=document.getElementById(k);clsDragdealer.aiMin||(clsDragdealer.aiMin=[]);clsDragdealer.aiMin[c]=e;clsDragdealer.aiMin[l]=
h;clsDragdealer.aiMax||(clsDragdealer.aiMax=[]);clsDragdealer.aiMax[c]=f;clsDragdealer.aiMax[l]=n;clsDragdealer.aiStep||(clsDragdealer.aiStep=[]);clsDragdealer.aiStep[c]=g;clsDragdealer.aiStep[l]=p},sbSetValueXY:function(a,b,c,d,e){clsDragdealer.sbSetValueDdXY(a,b,c,d,e);clsDragdealer.sbSetValueText(b,c);clsDragdealer.sbSetValueText(d,e)},sbSetValueDdXY:function(a,b,c,d,e){c=clsDragdealer.fnAdjustValue(b,c);e=clsDragdealer.fnAdjustValue(d,e);clsDragdealer.addMain[a].setValue((c-clsDragdealer.aiMin[b])/
(clsDragdealer.aiMax[b]-clsDragdealer.aiMin[b]),(e-clsDragdealer.aiMin[d])/(clsDragdealer.aiMax[d]-clsDragdealer.aiMin[d]))},sbSetValueText:function(a,b){b=clsDragdealer.fnAdjustValue(a,b);clsDragdealer.atxtMain[a].value=b},fnAdjustValue:function(a,b){var c=clsDragdealer.aiMin[a],d=clsDragdealer.aiStep[a];1<d?c+=Math.floor((b-c)/d)*d:(d=Math.floor(1/d),c+=Math.floor((b-c)*d)/d);return c},fnGetValue:function(a,b){return b?a.toLowerCase()+clsDragdealer.atxtMain[a].value:Number(clsDragdealer.atxtMain[a].value)}};
var clsColor=clsColor||{};clsColor={atxtMain:null,sbInit:function(a,b){clsColor.atxtMain||(clsColor.atxtMain=[]);clsColor.atxtMain[a]=document.getElementById(b)},sbSetValue:function(a,b){b=clsColor.fnAdjustValue(a,b);clsColor.atxtMain[a].value=b;jscolor.fireEvent(clsColor.atxtMain[a],"keyup")},fnGetValue:function(a,b){return(b?a.toLowerCase():"")+clsColor.atxtMain[a].value},fnAdjustValue:function(a,b){b.match(/[^0-9A-F]/g)&&(b="000000");return b}};var clsDot=clsDot||{};
clsDot={atxtMain:null,fnBit2XY:function(a,b,c){a=a.substr(0,b*c);b=[];for(var d=[],e=0,f=0,g=a.length;f<g;f++)"1"==a.substr(f,1)&&(d[e]=f%c,b[e]=Math.floor(f/c),e++);return{aiX:b,aiY:d}},fnCode2Bit:function(a){for(var b="",c=0,d=a.length;c<d;c++){var e=clsDot.fnAlphabet2Num(a,c);b+=("00000"+e.toString(2)).slice(-6)}return b},fnBit2Code:function(a){var b="",c=6-a.length%6;if(6>c)for(var d=0;d<c;d++)a+="0";d=0;for(c=a.length;d<c;d+=6){var e=a.substr(d,6);e=parseInt(e,2);b+=clsDot.fnNum2Alphabet(e)}return b},
fnNum2Alphabet:function(a){var b=0;0<=a&&9>=a?b=a+48:10<=a&&35>=a?b=a+97-10:36<=a&&61>=a?b=a+65-36:62==a?b=a+45-62:63==a&&(b=a+95-63);return String.fromCharCode(b)},fnAlphabet2Num:function(a,b){var c=a.charCodeAt(b),d=0;48<=c&&57>=c?d=c-48:97<=c&&122>=c?d=c-97+10:65<=c&&90>=c?d=c-65+36:45==c?d=c-45+62:95==c&&(d=c-95+63);return d}};var clsMorph=clsMorph||{};
clsMorph={iPanelW:0,iPanelPer:0,sShape:null,iFocusX:0,iFocusY:0,iFocusSize:0,iFocusAngle:0,iLw:0,strLc:"",iLp:0,strFc:"",iFp:0,iTr:0,strTc:"",sbLineTo:function(a,b,c){for(var d=b.length,e=0;e<d;e++)a.lineTo(b[e],c[e])},sbMoveToLineTo:function(a,b,c){var d=b.length;if(0<d){a.moveTo(b[0],c[0]);for(var e=1;e<d;e++)a.lineTo(b[e],c[e])}},sbMoveToBezierCurveTo:function(a,b,c){var d=b.length;if(0<d){a.moveTo(b[0],c[0]);for(var e=1;e<d;e+=3)a.bezierCurveTo(b[e],c[e],b[e+1],c[e+1],b[e+2],c[e+2])}},fnAdjustSVG:function(a,
b,c,d,e){var f=a.split(" "),g=f.length;a="";for(var l=0;l<g;l++){var k="";if(""!=f[l]&&0!=f[l].length)if(1==f[l].length)k=f[l];else if(7==f[l].length&&"#"==f[l].substring(0,1))k=f[l];else{var h=f[l].split(",");k=Number(h[0]);h=Number(h[1]);k=(k+b)*d;h=(h+c)*e;k=k+","+h}a+=(""!=a&&""!=k?" ":"")+k}return a},fnGetSVGXY:function(a,b,c,d){for(var e=a.split(" "),f=b.split(" "),g=e.length,l=0,k=0,h=0,n=0;n<g;n++)if(!(1>=e[n].length||7==e[n].length&&"#"==e[n].substring(0,1))){if(h==d){0==c||""==b?(a=e[n].split(","),
l=Number(a[0]),k=Number(a[1])):1==c||""==a?(f=f[n].split(","),l=Number(f[0]),k=Number(f[1])):(a=e[n].split(","),l=Number(a[0]),a=Number(a[1]),f=f[n].split(","),n=Number(f[1]),l=Math.round(l+(Number(f[0])-l)*c),k=Math.round(a+(n-a)*c));break}h++}return{iX:l,iY:k}},sbDrawMorphSVG:function(a,b,c,d,e,f,g,l,k,h){void 0===k&&(k=0);void 0===h&&(h=0);d=0>d?0:1<d?1:d;var n=[],p=0,m=b.split(" "),r=c.split(" "),t=m.length,q=""!=e||0<f&&0<g?0:1,u=""!=e||0<l?2:1;for(f*=0<f&&0<g&&0<l?2:1;q<u;q++){0==q?(a.lineWidth=
f,a.globalAlpha=""!=e?1:g):1==q&&(a.globalAlpha=""!=e?1:l);for(var A="",v=0;v<t;v++)if(""!=m[v]&&0!=m[v].length)if(1==m[v].length)A=m[v],"M"!=A&&("C"==A?p=0:"L"!=A&&"z"==A&&(0==q?a.stroke():1==q&&a.fill()));else if(7==m[v].length&&"#"==m[v].substring(0,1)){var w=0==d||""==c?m[v]:1==d||""==b?r[v]:clsMorph.fnGetMorphColor(m[v],r[v],d);0==q?(""!=e&&(w="#"+clsMorph.fnGetMorphColor(e,w,g)),a.strokeStyle=w):1==q&&(""!=e&&(w="#"+clsMorph.fnGetMorphColor(e,w,l)),a.fillStyle=w)}else{if(0==d||""==c){var z=
m[v].split(",");w=Number(z[0]);z=Number(z[1])}else if(1==d||""==b)z=r[v].split(","),w=Number(z[0]),z=Number(z[1]);else{z=m[v].split(",");w=Number(z[0]);var y=Number(z[1]);z=r[v].split(",");var x=Number(z[1]);w=Math.round(w+(Number(z[0])-w)*d);z=Math.round(y+(x-y)*d)}w+=k;z+=h;"M"==A?(a.beginPath(),a.moveTo(w,z)):"C"==A?(n[2*p+0]=w,n[2*p+1]=z,p++,3==p&&a.bezierCurveTo(n[0],n[1],n[2],n[3],n[4],n[5])):"L"==A&&a.lineTo(w,z)}}},sbAnimeBezierCurveOnly:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,q){""==t&&(t=
h);1==q||null==clsMorph.sShape?(clsMorph.sbDrawBezierCurveOnly(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,t),clsMorph.iPanelW=b,clsMorph.iPanelPer=c,clsMorph.sShape=d,clsMorph.iFocusX=e,clsMorph.iFocusY=f,clsMorph.iFocusSize=g,clsMorph.iFocusAngle=l,clsMorph.iLw=k,clsMorph.strLc=h,clsMorph.iLp=n,clsMorph.strFc=p,clsMorph.iFp=m,clsMorph.iTr=r,clsMorph.strTc=t):(b=clsMorph.iPanelW+(b-clsMorph.iPanelW)*q,c=clsMorph.iPanelPer+(c-clsMorph.iPanelPer)*q,d=clsMorph.fnGetMophPath(clsMorph.sShape,d,q),e=clsMorph.iFocusX+
(e-clsMorph.iFocusX)*q,f=clsMorph.iFocusY+(f-clsMorph.iFocusY)*q,g=clsMorph.iFocusSize+(g-clsMorph.iFocusSize)*q,l=clsMorph.iFocusAngle+(l-clsMorph.iFocusAngle)*q,k=clsMorph.iLw+(k-clsMorph.iLw)*q,h=clsMorph.fnGetMorphColor(clsMorph.strLc,h,q),n=clsMorph.iLp+(n-clsMorph.iLp)*q,p=clsMorph.fnGetMorphColor(clsMorph.strFc,p,q),m=clsMorph.iFp+(m-clsMorph.iFp)*q,r=clsMorph.iTr+(r-clsMorph.iTr)*q,t=clsMorph.fnGetMorphColor(clsMorph.strTc,t,q),clsMorph.sbDrawBezierCurveOnly(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t))},
sbGetPath:function(a,b,c,d,e,f,g){b=Math;for(var l=[],k=[],h=0,n=c.aiX.length;h<n;h++){l[h]=c.aiX[h];k[h]=c.aiY[h];if(0!=g){var p=b.sqrt(b.pow(l[h]-0,2)+b.pow(k[h]-0,2)),m=b.atan2(k[h]-0,l[h]-0)/(b.PI/180);m-=g;l[h]=0+b.cos(m/180*b.PI)*p;k[h]=0+b.sin(m/180*b.PI)*p}l[h]=(l[h]+(f/2+d))*a/f;k[h]=(k[h]+(f/2+e))*a/f}return{aiX:l,aiY:k}},sbDrawBezierCurveOnly:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,q){void 0===h&&(h="");void 0===p&&(p="");q=q||!1;var u=0<k&&0<n,A=0<m,v=0<r,w=[],z=[];if(u||A||v){e=(g/2+e)*
b/g;f=(g/2+f)*b/g;a.translate(e,f);0!=l%360&&a.rotate(-l*Math.PI/180);var y=d.aiX.length;3<y&&(y=3*Math.floor((y-1)/3)+1);for(var x=0;x<y;x++)w[x]=d.aiX[x]*b/g,z[x]=d.aiY[x]*b/g;if(v){a.fillStyle="#"+t;a.globalAlpha=1;a.beginPath();for(x=0;x<y;x++)a.moveTo(w[x]+r*c,z[x]),a.arc(w[x],z[x],r*c,0,2*Math.PI,!1);a.fill();a.lineWidth=r*c*.5;a.strokeStyle="#"+t;a.globalAlpha=1;a.beginPath();for(x=0;x<y;x++)q&&x<y-2&&w[x]==w[x+1]&&z[x]==z[x+1]&&w[x]==w[x+2]&&z[x]==z[x+2]&&(x+=3,a.moveTo(w[x],z[x])),0==x||
2==x%3?a.moveTo(w[x],z[x]):a.lineTo(w[x],z[x]);a.stroke()}if(u||A){a.lineWidth=k*c;if(q)for(a.beginPath(),c=b=0,0<w.length&&(b=w[0]+1),a.moveTo(w[0],z[0]),x=1;x<y;x+=3)d=w[x+2],g=z[x+2],w[x]==b&&z[x]==c&&w[x+1]==b&&z[x+1]==c?(A&&(a.fillStyle="#"+p,a.globalAlpha=m,a.fill()),u&&(a.strokeStyle="#"+h,a.globalAlpha=n,a.stroke()),a.beginPath(),a.moveTo(d,g)):(a.bezierCurveTo(w[x],z[x],w[x+1],z[x+1],w[x+2],z[x+2]),b=d,c=g);else a.beginPath(),clsMorph.sbMoveToBezierCurveTo(a,w,z);A&&(a.fillStyle="#"+p,a.globalAlpha=
m,a.fill());u&&(a.strokeStyle="#"+h,a.globalAlpha=n,a.stroke())}0!=l%360&&a.rotate(l*Math.PI/180);a.translate(-e,-f)}},sbDrawBezierCurveSimple:function(a,b,c){a.beginPath();clsMorph.sbMoveToBezierCurveTo(a,b.aiX,b.aiY)},fnGetMinArray:function(a){for(var b=0,c=0,d=a.length;c<d;c++)b=0==c||a[c]<b?a[c]:b;return b},fnGetMaxArray:function(a){for(var b=0,c=0,d=a.length;c<d;c++)b=0==c||a[c]>b?a[c]:b;return b},fnGetCenterArray:function(a){var b=clsMorph.fnGetMinArray(a);a=clsMorph.fnGetMaxArray(a);return b+
.5*(a-b)},fnGetCenterPath3d:function(a){var b=clsMorph.fnGetCenterArray(a.aiX),c=clsMorph.fnGetCenterArray(a.aiY);a=clsMorph.fnGetCenterArray(a.aiZ);return{iX:b,iY:c,iZ:a}},fnGetPerspectiveSize3d:function(a,b,c){for(var d=b.aiX.length,e,f,g,l,k,h,n=0;n<d;n++){if(void 0!==b.aiX){var p=b.aiX[n]*a/c;isNaN(e)?e=p:p<e&&(e=p);isNaN(f)?f=p:p>f&&(f=p)}void 0!==b.aiY&&(p=b.aiY[n]*a/c,isNaN(g)?g=p:p<g&&(g=p),isNaN(l)?l=p:p>l&&(l=p));void 0!==b.aiZ&&(p=b.aiZ[n]*a/c,isNaN(k)?k=p:p<k&&(k=p),isNaN(h)?h=p:p>h&&
(h=p))}b=a=c=0;void 0!==e&&void 0!==f&&(c=Math.floor(f-e));void 0!==g&&void 0!==l&&(a=Math.floor(l-g));void 0!==k&&void 0!==h&&(b=Math.floor(h-k));e=c;e=e>a?e:a;e=e>b?e:b;return 1<e?e:1},fnGetXY3dOnly:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r){void 0===r&&(r="l");var t=[],q=[],u=[],A="c"==r?4:2;r=b.aiX.length;for(var v=0;v<r;v++)t[v]=(b.aiX[v]-g)*a/c,q[v]=(b.aiY[v]-l)*a/c,u[v]=(b.aiZ[v]-k)*a/c;for(v=0;v<r;v++)0>m?(a=Math.floor(v/A)*A+A-1,v!=a&&(t[v]=t[a]+(t[v]-t[a])*-m,q[v]=q[a]+(q[v]-q[a])*-m,u[v]=u[a]+
(u[v]-u[a])*-m)):1>m&&(a=Math.floor(v/A)*A,v!=a&&(t[v]=t[a]+(t[v]-t[a])*m,q[v]=q[a]+(q[v]-q[a])*m,u[v]=u[a]+(u[v]-u[a])*m));for(v=0;v<r;v++)0!=p%360&&(m=clsMorph.fnRotate(0,0,t[v],q[v],p),t[v]=m.iX,q[v]=m.iY),0!=h%360&&(m=clsMorph.fnRotate(0,0,q[v],u[v],h),q[v]=m.iX,u[v]=m.iY),0!=n%360&&(m=clsMorph.fnRotate(0,0,u[v],t[v],-n),u[v]=m.iX,t[v]=m.iY);for(v=0;v<r;v++)t[v]*=(-u[v]+d)/d,q[v]*=(-u[v]+d)/d,t[v]=e+t[v],q[v]=f+q[v];return{aiX:t,aiY:q}},sbDrawPanelBezierCurve:function(a,b,c,d,e,f,g){void 0===
g&&(g="");if(0<d&&0<f){var l=c.aiX.length;3<l&&(l=4*Math.floor(l/4));a.lineWidth=d*b;a.strokeStyle="#"+e;a.globalAlpha=f;a.beginPath();if("moveline"==g)for(b=0;b<l;b+=2)a.moveTo(c.aiX[b+0],c.aiY[b+0]),a.lineTo(c.aiX[b+1],c.aiY[b+1]);else for(b=0;b<l;b+=4)a.moveTo(c.aiX[b+0],c.aiY[b+0]),a.bezierCurveTo(c.aiX[b+1],c.aiY[b+1],c.aiX[b+2],c.aiY[b+2],c.aiX[b+3],c.aiY[b+3]);a.stroke()}},sbDrawPanelLine:function(a,b,c,d,e,f,g){if(0<d&&0<f){a.lineWidth=d*b;a.strokeStyle="#"+e;a.globalAlpha=f;a.beginPath();
b=c.aiX.length;for(d=0;d<b;d+=2)a.moveTo(c.aiX[d+0],c.aiY[d+0]),a.lineTo(c.aiX[d+1],c.aiY[d+1]);a.stroke()}},sbDrawBezierCurveOnly3d:function(a,b,c,d,e,f,g,l,k,h,n){void 0===h&&(h="888888");var p=[],m=[];if(0<k&&0<n){e=(g/2+e)*b/g;f=(g/2+f)*b/g;a.translate(e,f);0!=l%360&&a.rotate(-l*Math.PI/180);var r=d.aiX.length;r=4*Math.floor(r/4);for(var t=0,q=0;q<r;q+=4)if(-.01<=d.aiX[q]&&-.01<=d.aiX[q+3])for(var u=q;u<q+4;u++)p[u]=d.aiZ[u]*b/g,m[u]=d.aiY[u]*b/g,t++;a.lineWidth=k*c;a.beginPath();for(q=0;q<r;q+=
4)clsMorph.sbMoveToBezierCurveTo(a,[p[q],p[q+1],p[q+2],p[q+3]],[m[q],m[q+1],m[q+2],m[q+3]]);a.strokeStyle="#"+h;a.globalAlpha=n;a.stroke();0!=l%360&&a.rotate(l*Math.PI/180);a.translate(-e,-f)}},sbDrawLineOnly3d:function(a,b,c,d,e,f,g,l,k,h,n){void 0===h&&(h="888888");var p=[],m=[];if(0<k&&0<n){e=(g/2+e)*b/g;f=(g/2+f)*b/g;a.translate(e,f);0!=l%360&&a.rotate(-l*Math.PI/180);for(var r=d.aiX.length,t=0,q=0;q<r;q++)if(0<=d.aiX[q]&&0<=d.aiX[q+1])for(var u=q;u<q+2;u++)p[u]=d.aiZ[u]*b/g,m[u]=d.aiY[u]*b/g,
t++;a.lineWidth=k*c;a.beginPath();for(q=0;q<r;q++)clsMorph.sbMoveToLineTo(a,[p[q],p[q+1]],[m[q],m[q+1]]);a.strokeStyle="#"+h;a.globalAlpha=n;a.stroke();0!=l%360&&a.rotate(l*Math.PI/180);a.translate(-e,-f)}},sbGetPath3d:function(a,b,c,d,e,f,g,l,k,h,n,p){b=[];var m=[],r=[],t=c.aiX.length;3<t&&(t=4*Math.floor(t/4));for(var q=0;q<t;q++){b[q]=(c.aiX[q]-g)*a/d;m[q]=(c.aiY[q]-l)*a/d;r[q]=(c.aiZ[q]-k)*a/d;if(0!=p%360){var u=clsMorph.fnRotate(0,0,b[q],m[q],p);b[q]=u.iX;m[q]=u.iY}0!=h%360&&(u=clsMorph.fnRotate(0,
0,m[q],r[q],h),m[q]=u.iX,r[q]=u.iY);0!=n%360&&(u=clsMorph.fnRotate(0,0,r[q],b[q],-n),r[q]=u.iX,b[q]=u.iY)}for(q=0;q<t;q++)b[q]*=(-r[q]+a)/a,m[q]*=(-r[q]+a)/a;for(q=0;q<t;q++)b[q]=e+b[q],m[q]=f+m[q];return{aiX:b,aiY:m}},fnGetMophPath3d:function(a,b,c){var d=[],e=[],f=[];if(b.aiX.length!=a.aiX.length||b.aiY.length!=a.aiY.length||b.aiZ.length!=a.aiZ.length||b.aiX.length!=b.aiY.length||b.aiX.length!=b.aiZ.length||0==c)for(var g=0,l=a.aiX.length;g<l;g++)d[g]=a.aiX[g],e[g]=a.aiY[g],f[g]=a.aiZ[g];else if(1==
c)for(g=0,l=b.aiX.length;g<l;g++)d[g]=b.aiX[g],e[g]=b.aiY[g],f[g]=b.aiZ[g];else for(g=0,l=a.aiX.length;g<l;g++)d[g]=a.aiX[g]+(b.aiX[g]-a.aiX[g])*c,e[g]=a.aiY[g]+(b.aiY[g]-a.aiY[g])*c,f[g]=a.aiZ[g]+(b.aiZ[g]-a.aiZ[g])*c;return{aiX:d,aiY:e,aiZ:f}},fnConvXYtoXYZofCylinder3d:function(a,b,c,d,e,f,g){void 0===g&&(g=[1]);var l=g.length,k=[],h=[],n=[],p=[],m=0;if(1==b.length)for(var r=Math.floor((c[0]-b[0])/2),t=0;t<r;t+=3)for(iIdx2=0;4>iIdx2;iIdx2++)k[m]=a.aiX[b[0]+(t+iIdx2)],h[m]=a.aiY[b[0]+(t+iIdx2)],
n[m]=a.aiX[c[0]-(t+iIdx2)],p[m]=a.aiY[c[0]-(t+iIdx2)],m++;else for(r=c.length,t=0;t<r;t++)k[m]=a.aiX[b[t]],h[m]=a.aiY[b[t]],n[m]=a.aiX[c[t]],p[m]=a.aiY[c[t]],m++;a=[];b=[];c=[];r=[];var q=360/d,u=0;d=0;for(iAngle=270;630>iAngle;iAngle+=q){var A=!0;d<e.length&&(A=1==e[d]);for(t=0;t<m;t++){var v=.5*(n[t]-k[t]),w=h[t]+.5*(p[t]-h[t]),z=.5*(p[t]-h[t]),y=Math.sqrt(Math.pow(v,2)+Math.pow(z,2));a[u]=k[t]+.5*(n[t]-k[t])+Math.sin(iAngle/180*Math.PI)*v;b[u]=w+Math.sin(iAngle/180*Math.PI)*z;v=Math.floor((t+2)/
4);c[u]=Math.cos(iAngle/180*Math.PI)*y*(1==l?g[0]:v<l?g[v]:1);r[u]=A;u++}d++}for(t=g=0;t<=m;t+=4){A=g<f.length?1==f[g]:t<m;for(l=0;l<d;l++)k=!0,l<e.length&&(k=1==e[l]),h=!0,l<e.length&&(h=1==e[l+1%d]),n=l*m+t,p=(l+1)%d*m+t,a[u]=a[n],b[u]=b[n],c[u]=c[n],r[u]=A&&k&&h,u++,a[u]=a[n],b[u]=b[n],c[u]=c[n],r[u]=A&&k&&h,u++,a[u]=a[p],b[u]=b[p],c[u]=c[p],r[u]=A&&k&&h,u++,a[u]=a[p],b[u]=b[p],c[u]=c[p],r[u]=A&&k&&h,u++;g++}t=0;for(d=a.length;t<d;t++)e=a[t],a[t]=c[t],c[t]=e;e=[];f=[];m=[];t=u=0;for(d=a.length;t<
d;t++)r[t]&&(e[u]=a[t],f[u]=b[t],m[u]=c[t],u++);return{aiX:e,aiY:f,aiZ:m}},fnConvXYtoXYZofPlate3d:function(a,b,c){var d=[],e=[],f=[],g=[];g[-1]=void 0!==b?b:[1];g[1]=void 0!==c?c:g[-1];var l=[];l[-1]=g[-1].length;l[1]=g[1].length;for(var k=0,h=a.aiX.length,n=-1;1>=n;n+=2){var p=0;b=0;for(c=h-1;b<c;b++)for(var m=0;2>m;m++){1==m&&p++;var r=p*l[n]/(h-1);var t=Math.floor(r/1)%l[n];var q=(t+1)%l[n];r%=1;d[k]=a.aiX[b+m];e[k]=a.aiY[b+m];f[k]=.5*(g[n][t]+(g[n][q]-g[n][t])*r)*n;k++}}b=0;for(c=h;b<c;b++)d[k]=
d[2*b],e[k]=e[2*b],f[k]=f[2*b],k++,d[k]=d[2*(h-1)+2*b],e[k]=e[2*(h-1)+2*b],f[k]=f[2*(h-1)+2*b],k++;b=0;for(c=d.length;b<c;b++)a=d[b],d[b]=f[b],f[b]=a;return{aiX:d,aiY:e,aiZ:f}},fnGetPointSphere3d:function(a,b){for(var c=360/b,d=[],e=[],f=[],g=0,l=0;l<b/2;l++)for(var k=0;k<b;k++)if(0==l||0!=k&&2!=k){d[g]=Math.cos(k*c/180*Math.PI)*a;e[g]=Math.sin(k*c/180*Math.PI)*a;f[g]=0;var h=clsMorph.fnRotate(0,0,e[g],f[g],l*c);e[g]=h.iX;f[g]=h.iY;g++}return{aiX:d,aiY:e,aiZ:f}},fnGetR:function(a,b,c,d){return Math.sqrt(Math.pow(c-
a,2)+Math.pow(d-b,2))},fnGetS:function(a,b,c,d){return(Math.atan2(d-b,c-a)/(Math.PI/180)+360)%360},sbDrawBezierArcOnly:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,q,u,A){var v=0<p&&0<r,w=0<q,z=0<u,y=[],x=[];if(v||w||z){e=(g/2+e)*b/g;f=(g/2+f)*b/g;a.translate(e,f);0!=l%360&&a.rotate(-l*Math.PI/180);for(var B=0,C=d.aiX.length;B<C;B++)y[B]=d.aiX[B]*b/g,x[B]=d.aiY[B]*b/g;if(z){a.fillStyle="#"+A;a.globalAlpha=1;a.beginPath();B=0;for(C=y.length;B<C;B++)a.moveTo(y[B]+u*c,x[B]),a.arc(y[B],x[B],u*c,0,2*Math.PI,
!1);a.fill();a.lineWidth=u*c*.5;a.strokeStyle="#"+A;a.globalAlpha=1;a.beginPath();B=0;for(C=y.length;B<C;B++)0==B||2==B%3?a.moveTo(y[B],x[B]):a.lineTo(y[B],x[B]);a.stroke()}if(v||w){a.lineWidth=p*c;a.beginPath();b=y[0];d=x[0];B=1;for(C=y.length;B<C;B+=3)clsMorph.sbDrawBezierArc(a,b,d,y[B],x[B],y[B+1],x[B+1],y[B+2],x[B+2],k*c,h*c,n*c),b=y[B+2],d=x[B+2];w&&(a.fillStyle="#"+t,a.globalAlpha=q,a.fill());v&&(a.strokeStyle="#"+m,a.globalAlpha=r,a.stroke())}0!=l%360&&a.rotate(l*Math.PI/180);a.translate(-e,
-f)}},fnCopyPath:function(a){for(var b={aiX:[],aiY:[]},c=0,d=a.aiX.length;c<d;c++)b.aiX[c]=a.aiX[c],b.aiY[c]=a.aiY[c];return b},fnGetBezierLength:function(a,b,c){for(var d=[],e=c.length,f=0;f<e;f++)d[f]=0;var g=0,l=a.aiX[0],k=a.aiY[0];for(f=0;f<e;f++)0==c[f]&&(d[f]=g);for(var h=1,n=a.aiX.length;h<n;h+=3){f=clsMorph.fnTrimBezier(l,k,a.aiX[h],a.aiY[h],a.aiX[h+1],a.aiY[h+1],a.aiX[h+2],a.aiY[h+2],b,0-g,1E17);g+=f.iLength;for(f=0;f<e;f++)c[f]==h-1+3&&(d[f]=g);l=a.aiX[h+2];k=a.aiY[h+2]}return d},fnTrimBezierOnly:function(a,
b,c,d){for(var e=0,f=[],g=[],l=0,k=a.aiX[0],h=a.aiY[0],n=1,p=a.aiX.length;n<p;n+=3){k=clsMorph.fnTrimBezier(k,h,a.aiX[n],a.aiY[n],a.aiX[n+1],a.aiY[n+1],a.aiX[n+2],a.aiY[n+2],b,c-e,d);h=0;for(var m=k.aiX.length;h<m;h++)f[l]=k.aiX[h],g[l]=k.aiY[h],l++;e+=k.iLength;if(e>c+d)break;k=a.aiX[n+2];h=a.aiY[n+2]}1>f.length&&(e>c+d?(f[l]=a.aiX[a.aiX.length-1],g[l]=a.aiY[a.aiX.length-1]):(f[l]=a.aiX[0],g[l]=a.aiY[0]));return{aiX:f,aiY:g}},fnTrimBezier:function(a,b,c,d,e,f,g,l,k,h,n){var p=a>c?a-c:c-a,m=b>d?b-
d:d-b;var r=0+(p>m?p:m);p=c>e?c-e:e-c;m=d>f?d-f:f-d;r+=p>m?p:m;p=e>g?e-g:g-e;m=f>l?f-l:l-f;r=parseInt((r+(p>m?p:m))/k);r=4>r?4:r;k=[];p=[];for(var t=m=0,q=0,u=0,A=0;A<r;A++){var v=A/(r-1),w=0,z=0;var y=(1-v)*(1-v)*(1-v);w+=y*a;z+=y*b;y=3*v*(1-v)*(1-v);w+=y*c;z+=y*d;y=3*v*v*(1-v);w+=y*e;z+=y*f;y=v*v*v;w+=y*g;z+=y*l;u>=h&&(k[q]=w,p[q]=z,q++);0<A&&(u+=Math.sqrt(Math.pow(m-w,2)+Math.pow(t-z,2)));if(u>h+n)break;m=w;t=z}return{aiX:k,aiY:p,iLength:u}},fnExpandXY:function(a,b,c){for(var d=0;d<a.aiX.length;d++)a.aiX[d]*=
b,a.aiY[d]*=c;return{aiX:a.aiX,aiY:a.aiY}},fnTrimXY:function(a,b,c){for(var d=[],e=[],f=0,g=0;g<a.aiX.length;g++)g>=b&&g<=c&&(d[f]=a.aiX[g],e[f]=a.aiY[g],f++);return{aiX:d,aiY:e}},SmoothJoin:function(a,b,c){void 0===c&&(c=.5);for(var d=[],e=[],f=0,g=0;g<a.aiX.length;g++)d[f]=a.aiX[g],e[f]=a.aiY[g],f++;g=a.aiX[a.aiX.length-2];var l=a.aiY[a.aiX.length-2],k=a.aiX[a.aiX.length-1];a=a.aiY[a.aiX.length-1];var h=b.aiX[0],n=b.aiY[0],p=b.aiX[1],m=b.aiY[1],r=Math.sqrt(Math.pow(k-g,2)+Math.pow(a-l,2)),t=Math.sqrt(Math.pow(h-
k,2)+Math.pow(n-a,2)),q=Math.sqrt(Math.pow(p-h,2)+Math.pow(m-n,2));d[f]=k+(g-k)*-(t*c/r);e[f]=a+(l-a)*-(t*c/r);f++;d[f]=h+(p-h)*-(t*c/q);e[f]=n+(m-n)*-(t*c/q);f++;for(g=0;g<b.aiX.length;g++)d[f]=b.aiX[g],e[f]=b.aiY[g],f++;return{aiX:d,aiY:e}},sbDrawBezierArc:function(a,b,c,d,e,f,g,l,k,h,n,p){var m=b>d?b-d:d-b,r=c>e?c-e:e-c;var t=0+(m>r?m:r);m=d>f?d-f:f-d;r=e>g?e-g:g-e;t+=m>r?m:r;m=f>l?f-l:l-f;r=g>k?g-k:k-g;t=parseInt((t+(m>r?m:r))/h);t=4>t?4:t;for(h=0;h<t;h++){var q=h/(t-1);r=m=0;var u=(1-q)*(1-q)*
(1-q);m+=u*b;r+=u*c;u=3*q*(1-q)*(1-q);m+=u*d;r+=u*e;u=3*q*q*(1-q);m+=u*f;r+=u*g;u=q*q*q;m+=u*l;r+=u*k;u=h/(t-1);u=Math.abs(Math.cos(u*Math.PI));u=n+(p-n)*u;0<u&&(a.moveTo(m+u,r),a.arc(m,r,u,0,2*Math.PI,!1))}},sbDrawBezierLine:function(a,b,c,d,e,f,g,l,k,h){var n=b>d?b-d:d-b,p=c>e?c-e:e-c;var m=0+(n>p?n:p);n=d>f?d-f:f-d;p=e>g?e-g:g-e;m+=n>p?n:p;n=f>l?f-l:l-f;p=g>k?g-k:k-g;m=parseInt((m+(n>p?n:p))/h);m=4>m?4:m;for(h=0;h<m;h++){n=h/(m-1);var r=p=0;iTemp=(1-n)*(1-n)*(1-n);p+=iTemp*b;r+=iTemp*c;iTemp=3*
n*(1-n)*(1-n);p+=iTemp*d;r+=iTemp*e;iTemp=3*n*n*(1-n);p+=iTemp*f;r+=iTemp*g;iTemp=n*n*n;p+=iTemp*l;r+=iTemp*k;0==h?a.moveTo(p,r):a.lineTo(p,r)}},sbBezierCurve2Line:function(a){var b=2/3;iIdx=0;for(iForCnt=a.aiY.length-3;iIdx<iForCnt;iIdx+=3){var c=a.aiX[iIdx+0];var d=a.aiY[iIdx+0];var e=a.aiX[iIdx+1];var f=a.aiY[iIdx+1];var g=a.aiX[iIdx+2];var l=a.aiY[iIdx+2];var k=a.aiX[iIdx+3];var h=a.aiY[iIdx+3];var n=c+1*(k-c)/3;var p=d+1*(h-d)/3;n+=(e-n)*b;p+=(f-p)*b;a.aiX[iIdx+1]=n;a.aiY[iIdx+1]=p;n=c+2*(k-
c)/3;p=d+2*(h-d)/3;n+=(g-n)*b;p+=(l-p)*b;a.aiX[iIdx+2]=n;a.aiY[iIdx+2]=p}return a},sbDrawLineOnly:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,q){var u=0<k&&0<n,A=0<m,v=0<r,w=[],z=[];if(u||A||v){e=(g/2+e)*b/g;f=(g/2+f)*b/g;a.translate(e,f);0!=l%360&&a.rotate(-l*Math.PI/180);for(var y=0,x=d.aiX.length;y<x;y++)w[y]=d.aiX[y]*b/g,z[y]=d.aiY[y]*b/g;if(v){a.fillStyle="#"+t;a.globalAlpha=1;a.beginPath();y=0;for(x=w.length;y<x;y++)a.moveTo(w[y]+r*c,z[y]),a.arc(w[y],z[y],r*c,0,2*Math.PI,!1);a.fill()}if(u||A){a.lineWidth=
k*c;if(q)for(a.beginPath(),d=c=b=0,0<w.length&&(c=w[0]+1),y=0,x=w.length;y<x;y++)g=w[y],k=z[y],0==b?(a.moveTo(g,k),b=1):g==c&&k==d?(A&&(a.fillStyle="#"+p,a.globalAlpha=m,a.fill()),u&&(a.strokeStyle="#"+h,a.globalAlpha=n,a.stroke()),a.beginPath(),b=0):(a.lineTo(g,k),c=g,d=k);else a.beginPath(),clsMorph.sbMoveToLineTo(a,w,z);A&&(a.fillStyle="#"+p,a.globalAlpha=m,a.fill());u&&(a.strokeStyle="#"+h,a.globalAlpha=n,a.stroke())}0!=l%360&&a.rotate(l*Math.PI/180);a.translate(-e,-f)}},sbDrawArc:function(a,
b,c,d,e,f,g){a.beginPath();a.arc(b,c,d,f/180*Math.PI,g/180*Math.PI,!1);a.arc(b,c,e,g/180*Math.PI,f/180*Math.PI,!0);a.closePath()},sbGetExtendLine:function(a,b,c,d,e,f){var g=Math.sqrt(Math.pow(c-a,2)+Math.pow(d-b,2));iX2=c+(a-c)*(1+e/g);iY2=d+(b-d)*(1+e/g);iX3=a+(c-a)*(1+f/g);iY3=b+(d-b)*(1+f/g);return[iX2,iY2,iX3,iY3]},sbGetGumLine:function(a,b,c,d,e,f,g,l){for(var k=[],h=[],n=Math.sqrt(Math.pow(c-a,2)+Math.pow(d-b,2)),p=Math.atan2(d-b,c-a)/(Math.PI/180),m=0,r=0;5>r;r++){var t=r%4,q=(2>t?a:c)+Math.cos((p+
90*(1==t||2==t?-1:1))/180*Math.PI)*(2>t?e:f)/2;t=(2>t?b:d)+Math.sin((p+90*(1==t||2==t?-1:1))/180*Math.PI)*(2>t?e:f)/2;0!=r&&(k[m]=0,h[m]=0,m++,k[m]=0,h[m]=0,m++);k[m]=q;h[m]=t;m++}k[1]=k[9]+(k[0]-k[9])*(1+e/n*.67);h[1]=h[9]+(h[0]-h[9])*(1+e/n*.67);k[2]=k[6]+(k[3]-k[6])*(1+e/n*.67);h[2]=h[6]+(h[3]-h[6])*(1+e/n*.67);k[7]=k[3]+(k[6]-k[3])*(1+f/n*.67);h[7]=h[3]+(h[6]-h[3])*(1+f/n*.67);k[8]=k[0]+(k[9]-k[0])*(1+f/n*.67);h[8]=h[0]+(h[9]-h[0])*(1+f/n*.67);k[4]=k[3]+.33*(k[6]-k[3]);h[4]=h[3]+.33*(h[6]-h[3]);
k[5]=k[3]+.67*(k[6]-k[3]);h[5]=h[3]+.67*(h[6]-h[3]);k[10]=k[9]+.33*(k[0]-k[9]);h[10]=h[9]+.33*(h[0]-h[9]);k[11]=k[9]+.67*(k[0]-k[9]);h[11]=h[9]+.67*(h[0]-h[9]);for(r=0;13>r;r++)e=clsMorph.fnRotate(5<=r&&10>=r?c:a,5<=r&&10>=r?d:b,k[r],h[r],5<=r&&10>=r?l:g),k[r]=e.iX,h[r]=e.iY;return{aiX:k,aiY:h}},fnRotate:function(a,b,c,d,e){if(0!=e%360){var f=Math.sqrt(Math.pow(c-a,2)+Math.pow(d-b,2));d=Math.atan2(d-b,c-a)/(Math.PI/180);d+=e;c=a+Math.cos(d/180*Math.PI)*f;d=b+Math.sin(d/180*Math.PI)*f}return{iX:c,
iY:d}},fnRotateArray:function(a,b,c,d,e,f){void 0===e&&(e=0);void 0===f&&(f=a.aiX.length-1);if(0!=d%360)for(;e<=f;e++){var g=Math.sqrt(Math.pow(a.aiX[e]-b,2)+Math.pow(a.aiY[e]-c,2)),l=Math.atan2(a.aiY[e]-c,a.aiX[e]-b)/(Math.PI/180);l+=d;a.aiX[e]=b+Math.cos(l/180*Math.PI)*g;a.aiY[e]=c+Math.sin(l/180*Math.PI)*g}return{aiX:a.aiX,aiY:a.aiY}},fnGetBright:function(a){void 0===a&&(a="");a=a.replace("#","");a=clsMorph.fnGetColor16to10(a);return Math.sqrt(.241*Math.pow(a.iR/255,2)+.691*Math.pow(a.iG/255,2)+
.068*Math.pow(a.iB/255,2))},fnAdjustBright:function(a,b){void 0===a&&(a="");a=a.replace("#","");var c=clsMorph.fnGetBright(a);return c>=b?clsMorph.fnGetMorphColor("000000",a,b/c):clsMorph.fnGetMorphColor(a,"ffffff",(b-c)/(1-c))},fnRoundColor:function(a,b){void 0===a&&(a="");a=a.replace("#","");var c=clsMorph.fnGetColor16to10(a);var d=Math.round(c.iR/b)*b,e=Math.round(c.iG/b)*b;c=Math.round(c.iB/b)*b;return clsMorph.fnGetColor10to16(255>d?d:255,255>e?e:255,255>c?c:255)},fnGetMorphColor:function(a,
b,c){void 0===a&&(a="");void 0===b&&(b="");a=a.replace("#","");b=b.replace("#","");if(""==a&&""==b)return"";if(""==a)return b;if(""==b)return a;a=clsMorph.fnGetColor16to10(a);b=clsMorph.fnGetColor16to10(b);return clsMorph.fnGetColor10to16(Math.round(a.iR+(b.iR-a.iR)*c),Math.round(a.iG+(b.iG-a.iG)*c),Math.round(a.iB+(b.iB-a.iB)*c))},fnGetColor16to10:function(a){a=a.replace("#","");var b=parseInt(a.substring(0,2),16),c=parseInt(a.substring(2,4),16);a=parseInt(a.substring(4,6),16);return{iR:b,iG:c,iB:a}},
fnGetColor10to16:function(a,b,c){a=("0"+parseInt(a).toString(16)).slice(-2);b=("0"+parseInt(b).toString(16)).slice(-2);c=("0"+parseInt(c).toString(16)).slice(-2);return(a+b+c).toUpperCase()},fnGetMophPath:function(a,b,c){var d=[],e=[];if(b.aiX.length!=a.aiX.length||b.aiY.length!=a.aiY.length||b.aiX.length!=b.aiY.length||0==c)for(var f=0,g=a.aiX.length;f<g;f++)d[f]=a.aiX[f],e[f]=a.aiY[f];else if(1==c)for(f=0,g=b.aiX.length;f<g;f++)d[f]=b.aiX[f],e[f]=b.aiY[f];else for(f=0,g=a.aiX.length;f<g;f++)d[f]=
a.aiX[f]+(b.aiX[f]-a.aiX[f])*c,e[f]=a.aiY[f]+(b.aiY[f]-a.aiY[f])*c;return{aiX:d,aiY:e}},fnGetMophArray:function(a,b,c){var d=[];if(a.length!=b.length||0==c)for(var e=0,f=b.length;e<f;e++)d[e]=b[e];else if(1==c)for(e=0,f=a.length;e<f;e++)d[e]=a[e];else for(e=0,f=b.length;e<f;e++)d[e]=b[e]+(a[e]-b[e])*c;return d},fnAlignSVGLine2Line:function(a,b,c,d,e,f,g,l){var k=a.split(" "),h=k.length,n=[];n.aiX=[];n.aiY=[];for(var p=0;p<h;p++)0<=k[p].indexOf(",")&&(a=k[p].split(","),n.aiX[n.aiX.length]=Number(a[0]),
n.aiY[n.aiY.length]=Number(a[1]));clsMorph.fnAlignShapeLine2Line(n,b,c,d,e,n.aiX[f],n.aiY[f],n.aiX[g],n.aiY[g],l);b=0;a="";for(p=0;p<h;p++)a+=""==a?"":" ",0<=k[p].indexOf(",")?(a+=n.aiX[b]+","+n.aiY[b],b++):a+=k[p];return a},fnAlignShapeLine2Line:function(a,b,c,d,e,f,g,l,k,h){if(h){h=0;for(var n=a.aiX.length;h<n;h++)a.aiX[h]*=-1;f*=-1;l*=-1}var p=Math.sqrt(Math.pow(d-b,2)+Math.pow(e-c,2))/Math.sqrt(Math.pow(l-f,2)+Math.pow(k-g,2));d=Math.atan2(k-g,l-f)/(Math.PI/180)-Math.atan2(e-c,d-b)/(Math.PI/180);
h=0;for(n=a.aiX.length;h<n;h++)e=clsMorph.fnRotate(0,0,a.aiX[h]-f,a.aiY[h]-g,0-d),a.aiX[h]=b+e.iX*p,a.aiY[h]=c+e.iY*p;return{aiX:a.aiX,aiY:a.aiY}},sbAlignShapePoint2Point:function(a,b,c,d,e){b=d-b;c=e-c;e=0;for(d=a.aiX.length;e<d;e++)a.aiX[e]-=b,a.aiY[e]-=c;return{aiX:a.aiX,aiY:a.aiY}},fnGetBezierCurveOnlySVG:function(a,b){for(var c="",d=0,e=a.length;d<e;d++)0==d?c+="M":1==d%3&&(c+=" C"),c+=" "+Math.floor(1*a[d]),c+=","+Math.floor(1*b[d]);return c},fnGetLabelLocate:function(a,b,c,d,e,f,g,l,k){for(var h,
n=Math.floor((a-a*l*2)/f),p=Math.floor((b-b*l*2)/g),m=[],r=h=0;r<g;r++)for(var t=0;t<f;t++){m[h]={};m[h].iX=a*l+n*t;m[h].iY=b*l+p*r;m[h].iHit=0;m[h].iLayerIdx=-1;for(var q=d;q<e+1;q++)for(var u=0,A=c[q].aiX.length;u<A;u++)iPathX=c[q].aiX[u],iPathY=c[q].aiY[u],iPathX>=m[h].iX&&iPathX<=m[h].iX+n&&iPathY>=m[h].iY&&iPathY<=m[h].iY+p&&(m[h].iHit+=1);h+=1}A=h;for(q=0;2>q;q++){for(h=0;h<A;h++)m[h].iRin=0;for(r=h=0;r<g;r++)for(t=0;t<f;t++)0<t&&(m[h-1].iRin+=m[h].iHit),t<f-1&&(m[h+1].iRin+=m[h].iHit),0<r&&
(m[h-f].iRin+=m[h].iHit),r<g-1&&(m[h+f].iRin+=m[h].iHit),h+=1;for(h=0;h<A;h++)m[h].iHit=10*m[h].iHit+m[h].iRin,m[h].iRIn=0}m.sort(function(a,b){return a.iHit-b.iHit});aiLayer2Block=[];for(q=d;q<e+1;q++)aiLayer2Block[q]=-1;for(q=0;q<e-d+1;q++){r=-1;for(f=d;f<e+1;f++)for(h=0;h<e-d+1;h++)if(-1==aiLayer2Block[f]&&-1==m[h].iLayerIdx)for(g=0,A=c[f].aiX.length;g<A;g++){u=c[f].aiX[g];var v=c[f].aiY[g];t=Math.sqrt(Math.pow(m[h].iX+0-u,2)+Math.pow(m[h].iY+0-v,2));b=Math.sqrt(Math.pow(m[h].iX+n-u,2)+Math.pow(m[h].iY+
0-v,2));l=Math.sqrt(Math.pow(m[h].iX+0-u,2)+Math.pow(m[h].iY+p-v,2));u=Math.sqrt(Math.pow(m[h].iX+n-u,2)+Math.pow(m[h].iY+p-v,2));if(-1==r||t<r||b<r||l<r||u<r){r=t;r=b<r?b:r;r=l<r?l:r;r=u<r?u:r;var w=h;var z=f}}m[w].iLayerIdx=z;aiLayer2Block[z]=w}c=[];for(q=d;q<e+1;q++)h=aiLayer2Block[q],c[q]={},c[q].iX=m[h].iX+a*k,c[q].iY=m[h].iY+a*k,c[q].iW=n-a*k*2,c[q].iH=p-a*k*2;return c},fnGetLayoutXY:function(a,b,c,d,e,f,g,l,k,h,n,p,m){a+=e;b+=e;c=Math.floor((c-2*e-f*(g+1))/g);d=Math.floor((d-2*e-f*(l+1))/l);
e={};e.iX=f+a+(c+f)*k;e.iY=f+b+(d+f)*h;e.iW=c*n+f*(n-1);e.iH=d*p+f*(p-1);if(m)for(m.lineWidth=3,m.globalAlpha=.2,m.fillStyle="#ff8888",m.beginPath(),m.rect(e.iX,e.iY,e.iW,e.iH),m.fill(),k=0;k<l;k++)for(h=0;h<g;h++)iTempX=f+a+(c+f)*h,iTempY=f+b+(d+f)*k,iTempW=c,iTempH=d,m.strokeStyle="#00ffff",m.beginPath(),m.rect(iTempX,iTempY,iTempW,iTempH),m.stroke(),m.strokeStyle="#00ff00",m.beginPath(),m.moveTo(iTempX,iTempY),m.lineTo(iTempX+iTempW,iTempY+iTempH),m.moveTo(iTempX+iTempW,iTempY),m.lineTo(iTempX,
iTempY+iTempH),m.stroke();return e}};var clsGraph=clsGraph||{};
clsGraph={iDrawRadarLast:0,iDrawTableLast:0,End:null,sbDrawGraphPaper:function(a,b,c,d,e,f,g){e="#"+e.replace("#","");a.lineWidth=d;a.strokeStyle=e;a.globalAlpha=f;for(d=b%g/2;d<b;d+=g)a.beginPath(),a.moveTo(d,0),a.lineTo(d,c),a.stroke();for(d=c%g/2;d<c;d+=g)a.beginPath(),a.moveTo(0,d),a.lineTo(b,d),a.stroke()},sbDrawRadar:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,q,u,A,v){0>=v&&(clsGraph.iDrawRadarLast=0);m="#"+m.replace("#","");t="#"+t.replace("#","");u="#"+u.replace("#","");var w=.4*g,z=.2*l;e+=g/
2;f+=l/2;l=l/2*.65;k=k.split(",");h=h.split(",");n=n.split(",");g=k.length;for(var y=0;y<h.length;y++)h[y]=Number(h[y]);for(y=0;y<n.length;y++)n[y]=Number(n[y]);var x=Math.floor(g*v);v=g*v%1*3-1;v=1<v?1:v;x>=g&&(x=g-1,v=1,0==clsGraph.iDrawRadarLast&&(a=b,c=d,clsGraph.iDrawRadarLast=1));d=b="";for(y=0;y<g;y++)b+=(0==y?"":",")+(y<=x?k[y]:""),d+=(0==y?"":",")+Math.floor(n[y]*(y<x?1:y>x?0:v));k=b.split(",");n=d.split(",");for(y=0;y<n.length;y++)n[y]=Number(n[y]);b="";for(y=0;5>y;y++){switch(y){case 0:a.fillStyle=
u;a.globalAlpha=A;a.beginPath();break;case 1:a.lineWidth=r;a.strokeStyle=t;a.globalAlpha=q;a.beginPath();break;case 2:a.lineWidth=r;a.strokeStyle=t;a.globalAlpha=q;break;case 3:a.lineWidth=r,a.strokeStyle=u,a.globalAlpha=q,a.beginPath()}for(d=0;d<g;d++){switch(y){case 0:var B=(0>n[d]?0:n[d])/h[d%h.length]*l;break;case 1:B=l;break;case 2:B=l;break;case 3:B=(0>n[d]?0:n[d])/h[d%h.length]*l;break;case 4:B=1.3*l}v=e+Math.round(Math.cos((360/g*d+270)/180*Math.PI)*B);x=f+Math.round(Math.sin((360/g*d+270)/
180*Math.PI)*B);switch(y){case 0:0==d?a.moveTo(v,x):a.lineTo(v,x);break;case 1:0==d?a.moveTo(v,x):a.lineTo(v,x);break;case 2:a.beginPath();a.moveTo(e,f);a.lineTo(v,x);a.stroke();break;case 3:0==d?a.moveTo(v,x):a.lineTo(v,x);break;case 4:b+=clsPanel.fnGetTableText(v-w/2,x-z/2,w,z,"c",p,t,k[d]+"<br />"+(""==k[d]||0>n[d]?"&nbsp;":'<span style="color: '+m+';">'+n[d])+"</span>")}}switch(y){case 0:a.closePath();a.fill();break;case 1:a.closePath();a.stroke();break;case 3:a.closePath(),a.stroke()}}c.innerHTML+=
b},sbDrawTable:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,q,u,A,v,w,z,y,x){if(0>=x)clsGraph.iDrawTableLast=0;else{p=p.split(":");m=m.split(":");var B=r.split(","),C=q.split(","),E=A.split(","),F=w.split(",");w=p.length;A=[];for(q=0;q<w;q++)A[q]=e,p[q]=(g-k*(w-1))*Number(p[q]),e+=p[q]+k;g=B.length;k=[];e=[];q=[];r=[];for(var G=[],H=[],D=0;D<g;D++)k[D]=B[D].split(":"),e[D]=C[D%C.length].split(":"),q[D]=E[D%E.length].split(":"),r[D]=F[D%F.length].split(":"),H[D]=f,G[D]=(l-h*(g-1))/g,f+=G[D]+h;h=w*g;l=Math.floor(h*
x);x=h*x%1*3-1;x=0>x?0:x;x=1<x?1:x;for(h=clsGraph.iDrawTableLast;h<=l;h++){f=h<l?b:a;B=h<l?d:c;E=C=0;"cell-dr"==y?(C=Math.floor(h/g),E=h%g):"cell-rd"==y&&(C=h%w,E=Math.floor(h/w));if(h<l||0<x){var I=e[E][C%e[E].length];F=q[E][C%q[E].length];D=r[E][C%r[E].length];I="#"+I.replace("#","");F="#"+F.replace("#","");D="#"+D.replace("#","");f.beginPath();f.rect(A[C],H[E],p[C],G[E]*(h<l?1:x));f.lineWidth=u;f.strokeStyle=F;f.globalAlpha=v;f.stroke();f.fillStyle=D;f.globalAlpha=z;f.fill()}if(h<l||1==x)B.innerHTML+=
clsPanel.fnGetTableText(A[C]+n,H[E],p[C]-2*n,G[E],m[C%m.length],t,I,k[E][C])}l>clsGraph.iDrawTableLast&&(clsGraph.iDrawTableLast=l)}}};var clsSocial=clsSocial||{};
clsSocial={sbTwitter:function(a,b){var c,d=a.getElementsByTagName(b)[0];(function(e,f,g){a.getElementById(f)||(c=a.createElement(b),c.src=e,c.async=!0,c.id=f,d.parentNode.insertBefore(c,d),window.ActiveXObject&&null!=g?c.onreadystatechange=function(){"complete"==c.readyState&&g();"loaded"==c.readyState&&g()}:c.onload=g)})("//platform.twitter.com/widgets.js","twitter-wjs")}};var clsAma=clsAma||{};
clsAma={m_strReqAma:"",strElm:"",strHtmlParent:"",strHtmlChild:"",iRowMax:0,bMustImage:!1,sbViewAma:function(a,b,c,d,e,f,g,l,k,h){if(!document.getElementById(f)||""==d)return!1;a=""+a+("?Timestamp="+(new Date).getTime());a=a+("&AssociateTag="+b)+("&SearchIndex="+c);a+="&Keywords="+d;a+="&Sort="+e;if(l.indexOf("{img-")||l.indexOf("{imgurl-"))a+="&ResponseGroup=Small,OfferSummary,Images";if(clsAma.m_strReqAma==a)return!1;clsAma.m_strReqAma=a;clsAma.strElm=f;clsAma.strHtmlParent=g;clsAma.strHtmlChild=
l;clsAma.iRowMax=k;clsAma.bMustImage=h;$.ajax({type:"GET",url:a,cache:!1,dataType:"xml",success:function(a,b,c){clsAma.fnDone(a)},error:function(a,b,c){clsAma.fnFail()}})},fnFail:function(){},fnDone:function(a){for(var b=["s","m","l"],c=clsAma.strHtmlChild.split("\n").length,d="",e=[],f=0;f<c;f++)e[f]="";if(a&&(clsAma.fnGetNodeValue(a,"Keywords"),a=a.getElementsByTagName("Item"),0<a.length))for(var g=0,l=0;l<a.length&&g<clsAma.iRowMax;l++){f=a.item(l);var k=clsAma.fnGetNodeValue(f,"DetailPageURL"),
h=clsAma.fnGetNodeValue(f,"Title"),n=clsAma.fnGetNodeValue(f,"FormattedPrice");n=n.replace(/ /g,"");var p=clsAma.strHtmlChild;p=p.replace(/\{url\}/g,k.replace(/\n/g,""));p=p.replace(/\{price\}/g,n.replace(/\n/g,""));p=p.replace(/\{title\}/g,h.replace(/\n/g,""));k=!1;h=0;for(n=b.length;h<n;h++){var m="";strImgSize=b[h];if(p.indexOf("{img-"+strImgSize+"}")||p.indexOf("{imgurl-"+strImgSize+"}")){var r=f.getElementsByTagName("s"==strImgSize?"SmallImage":"m"==strImgSize?"MediumImage":"LargeImage");0<r.length&&
(m=clsAma.fnGetNodeValue(r[0],"URL").replace(/\n/g,""),k=!0)}p=p.replace("{img-"+strImgSize+"}",'<img src="'+m+'" />');p=p.replace("{imgurl-"+strImgSize+"}",m)}clsAma.bMustImage&&0==k&&(p="");if(""!=p){d+=p;p=p.split("\n");for(f=0;f<c;f++)e[f]+=p[f];g++}}if(""!=d){b=clsAma.strHtmlParent;for(f=0;f<c;f++)b=b.replace("{"+f+"}",e[f]);document.getElementById(clsAma.strElm).innerHTML=b}},fnGetNodeValue:function(a,b){var c=a.getElementsByTagName(b),d="";0<c.length&&(d=c.item(0).firstChild.nodeValue);return d}};
var clsCommonMain=clsCommonMain||{};
clsCommonMain={astrCookieParam:[],strCookieHead:"",COOKIE_EXPIRES:7,COOKIE_PVCOUNT:"COOKIE_PVCOUNT",COOKIE_ADULT_EXPIRES:90,COOKIE_ADULT:"COOKIE_ADULT",iPv:0,End:null,sbInitCookie:function(a,b){clsCommonMain.strCookieHead=a;clsCommonMain.astrCookieParam=b},sbSetCookie:function(a,b){$.cookie(clsCommonMain.strCookieHead+a,b,clsCommonMain.astrCookieParam)},fnGetCookie:function(a){return $.cookie(clsCommonMain.strCookieHead+a)},sbOnloadCount:function(){null!=$.cookie(clsCommonMain.COOKIE_PVCOUNT)&&(clsCommonMain.iPv=
$.cookie(clsCommonMain.COOKIE_PVCOUNT));clsCommonMain.iPv=Number(clsCommonMain.iPv);clsCommonMain.iPv=(clsCommonMain.iPv+1)%1E5;$.cookie(clsCommonMain.COOKIE_PVCOUNT,clsCommonMain.iPv,{path:"/",expires:clsCommonMain.COOKIE_EXPIRES})},sbGetAdult:function(){var a=0;null!=$.cookie(clsCommonMain.COOKIE_ADULT)&&(a=$.cookie(clsCommonMain.COOKIE_ADULT));return a},sbSetAdult:function(a){$.cookie(clsCommonMain.COOKIE_ADULT,a,{path:"/",expires:clsCommonMain.COOKIE_ADULT_EXPIRES})},sbOnloadSocial:function(){clsSocial.sbTwitter(document,
"script")},sbOnloadAma:function(a,b,c,d,e,f){if(!document.getElementById(f))return!1;d=d.replace(/,,/g,",").replace(/^,/,"").replace(/,$/,"");if(""==d)return!1;d=d.split(",");d=d[Math.floor(Math.random()*d.length)];if(""==d)return!1;e=clsPanel.fnGetWindowWidth(0,160,640);e=Math.floor(e/160);if(1.5>Math.random()){var g="<table><tr>{0}</tr><tr>{1}</tr><tr>{2}</tr></table>";var l='<td class="bt"><div class="ct"><a target="_blank" href="{url}" target="_blank"><span class="contain" style="background-image: url({imgurl-m})"></span></a></div></td>\n<td class="tp"><div class="ct">{price}<div></td>\n<td class="tp"><a target="_blank" href="{url}" target="_blank">{title}</a></td>'}else g=
"<table><tr>{0}</tr></table>",l='<td class="bt"><div class="ct"><a target="_blank" href="{url}" target="_blank"><span class="contain" style="background-image: url({imgurl-m})"></span></a></div></td>';clsAma.sbViewAma(a,b,c,encodeURIComponent(d),"",f,g,l,e,!0)},fnGetWait:function(){return 2==clsCommonMain.iPv%200||32==clsCommonMain.iPv%200?2E3:0},fnParseRdCode:function(a){var b=[];if(void 0!==a)for(var c=0,d=a.length;c<d;c++)b[c]=Number(a.substr(c,1));return b},sbDrawStage:function(a,b,c,d,e,f,g){a.clearRect(0,
0,b,c);0<e.length&&(a.globalAlpha=1,a.fillStyle="#"+e,a.fillRect(0,0,b,c));0<f.length&&e!=f&&clsGraph.sbDrawGraphPaper(a,b,c,.5*d,f,1,b/g*10)},sbDrawFrame:function(a,b,c,d,e,f){e!=f&&(e=b/64,a.globalAlpha=1,a.lineWidth=1*d,a.strokeStyle="#"+f,a.beginPath(),a.moveTo(e,0),a.lineTo(e,c),a.moveTo(b-e,0),a.lineTo(b-e,c),a.moveTo(0,e),a.lineTo(b,e),a.moveTo(0,c-e),a.lineTo(b,c-e),a.stroke())},sbDrawSpeakBox:function(a,b,c,d,e,f,g,l,k,h,n,p,m){e=clsPanel.actxCv[1<=m?e:f];0<l&&""!=k&&0<h&&(e.lineWidth=Math.floor(l*
g),e.strokeStyle="#"+k,e.globalAlpha=h,e.strokeRect(a,b,c,d*m));""!=n&&0<p&&(e.fillStyle="#"+n,e.globalAlpha=p,e.fillRect(a,b,c,d*m))},sbDrawFlash:function(a,b,c,d,e,f){d=f*e%1+e/d;d=Math.sin((.8-.9*(1<d?1:d))/2*Math.PI);d=0>d?0:d;a.beginPath();a.rect(0,0,b,c);a.fillStyle="#FFFFFF";a.globalAlpha=d;a.fill()},fnGetSpeakTextHtml:function(a,b,c,d,e,f,g,l,k,h,n,p,m,r,t,q){l=l.replace("#","");if(1<=h&&(p=p.replace(/\{n\}/g,"<br />"),""!=p)){if(0<=p.indexOf("{d}"))for(h=0;h<m;h++)t[h]="";f=Math.floor(f*
clsPanel.iPer);g=Math.floor(g*clsPanel.iPer);h=0<=p.indexOf("{c}")||0>n?"":"color: #"+k[n].replace("#","")+";";g=0<=p.indexOf("{b}")?"font-size: "+g+"px;":"";k=0<=p.indexOf("{m}")?"c":"l";n=""!=h||g?'<span style="'+h+g+'">':"";g=""!=h||g?"</span>":"";p=p.replace(/\{(\d+)\}/g,"&#$1;");p=p.replace(/\{.*?\}/g,"");if(q){for(h=0;h<m-1;h++)t[h]=t[h+1];t[m-1]=""}t[m-1]+=n+p+g;q=0<=p.indexOf("<br />");p="";for(h=0;h<m;h++)p+=t[h];r=0>c||0>d?p:clsPanel.fnGetTableText(a+e,b,c-2*e,d,k,f,l,p)}return{strHtml:r,
astrLabelText:t,bBreak:q}},fnGetTextHtml:function(a,b,c,d,e,f,g,l,k,h,n){if(1<=e&&(g=g.replace(/\{n\}/g,"<br />"),""!=g)){if(0<=g.indexOf("{d}"))for(e=0;e<l;e++)h[e]="";e=0<=g.indexOf("{c}")||0>f?"color: #"+c.replace("#","")+";":"color: #"+d[f].replace("#","")+";";c=0<=g.indexOf("{b}")?"font-size: "+b+"px;":"";g.indexOf("{m}");b=""!=e||c?'<span style="'+e+c+'">':"";c=""!=e||c?"</span>":"";g=g.replace(/\{(\d+)\}/g,"&#$1;");g=g.replace(/\{.*?\}/g,"");if(n){for(e=0;e<l-1;e++)h[e]=h[e+1];h[l-1]=""}h[l-
1]+=b+g+c;n=0<=g.indexOf("<br />");a=""+('<span style="font-size: '+a+'px;">');for(e=0;e<l;e++)a+=h[e];k=a+"</span>"}return{strHtml:k,astrLabelText:h,bBreak:n}}};var clsCommonHtml=clsCommonHtml||{};
clsCommonHtml={astrRealtimeCount:[],iRealtimeCount:0,End:null,sbInitRealtimeCount:function(){if(document.getElementById("elmRealtimeCount")){for(var a=document.getElementById("txtRealtimeCount").value.split("G"),b=0,c=a.length;b<c;b++){var d=parseInt(a[b],16);clsCommonHtml.astrRealtimeCount[b]=String(d).replace(/(\d)(?=(\d\d\d)+(?!\d))/g,"$1,")}clsCommonHtml.iRealtimeCount=0;clsCommonHtml.sbViewRealtimeCount();a=Number(document.getElementById("txtRealtimeViewSpan").value);setInterval("clsCommonHtml.sbViewRealtimeCount()",
1E3*a)}},sbViewRealtimeCount:function(){document.getElementById("elmRealtimeCount").innerHTML=clsCommonHtml.astrRealtimeCount[clsCommonHtml.iRealtimeCount];clsCommonHtml.iRealtimeCount<clsCommonHtml.astrRealtimeCount.length-1&&clsCommonHtml.iRealtimeCount++},sbShowDescStart4View:function(a){0==a?clsCommonHtml.sbShowDesc4View():(a=clsCommonMain.fnGetWait(),setTimeout("clsCommonHtml.sbShowDesc4Edit()",a))},sbShowDesc4View:function(){document.getElementById("elmDescView").style.display="block"},sbShowDescStart4Edit:function(){var a=
clsCommonMain.fnGetWait();setTimeout("clsCommonHtml.sbShowDesc4Edit()",a)},sbShowDesc4Edit:function(){document.getElementById("elmDescEdit").style.display="block"},sbDebug:function(){document.getElementById("msg").innerHTML=""+Math.random()},sbInitAdult:function(){document.getElementById("elmAdult").style.display="block"},sbClickAdultYes:function(a){document.getElementById("elmAdult").style.display="none";clsCommonMain.sbSetAdult(1);a()},sbClickAdultNo:function(){document.getElementById("elmAdult").style.display=
"none"}};var clsJquery=clsJquery||{};clsJquery={m_strReqAma:"",strElm:"",strHtmlParent:"",strHtmlChild:"",iRowMax:0,bMustImage:!1,sbInitAccordion:function(a,b,c){for(var d=0,e=$("#"+a+" "+c).length;d<e;d++)"block"!=$.cookie("accordion_"+a+d)&&"inline-block"!=$.cookie("accordion_"+a+d)||$("#"+a+d).next(c).show("fast");$("#"+a+" "+b).click(function(){var a=$(this).next(c),b=$(this).attr("id");$(a).slideToggle("fast",function(){$.cookie("accordion_"+b,$(a).css("display"),{expires:1})})})}};
var clsTab=clsTab||{};
clsTab.sbChangeTabAndPanel=function(a,b,c,d,e){var f=!1;d=d.split(";");for(var g=0,l=d.length;g<l;g++){var k=d[g],h=document.getElementById(c.replace("{0}",k));h&&(h.style.display=k==e?"block":"none");(h=document.getElementById(a.replace("{0}",k)))&&k==e&&(f=!0)}if(f)for(g=0,l=d.length;g<l;g++)if(k=d[g],h=document.getElementById(a.replace("{0}",k)))h.style.display=k==e?"inline":"none",document.getElementById(b.replace("{0}",k)).style.display=k==e?"none":"inline";$("html,body").animate({scrollTop:0},"slow")};
var clsAudio=clsAudio||{};
clsAudio={fnGet:function(a,b,c){var d=null;if(window.HTMLAudioElement){d=new Audio;d.autoplay=!1;for(var e=[{strExt:"mp3",strType:"audio/mpeg"},{strExt:"ogg",strType:"audio/ogg"},{strExt:"wav",strType:"audio/wav"}],f=0,g=e.length;f<g;f++)if(""!==d.canPlayType(e[f].strType)){d.src=a+b+"."+e[f].strExt+"?"+c;break}}return d},sbLoad:function(a){a&&(a.load(),a.muted=!0,a.volume=0,a.play())},sbPlay:function(a,b){a&&(a.muted=!1,a.volume=b,a.play())},sbPlayStart:function(a,b){a&&(a.muted=!1,a.volume=b,a.load(),
a.play())},sbPause:function(a){a&&a.pause()},sbStop:function(a){a&&!a.ended&&(a.pause(),a.currentTime=0)}};var clsVibe=clsVibe||{};
clsVibe={bVibe:!1,fnIsSupport:function(){var a=!1,b=navigator.userAgent;if(0<b.indexOf("iPhone")||0<b.indexOf("iPod")||0<b.indexOf("Android")||0<b.indexOf("iPad"))navigator.mozVibrate?a=!0:navigator.vibrate&&(a=!0);"localhost"==document.location.hostname&&(a=!0);return a},fnGetPattern:function(a,b,c){var d=[];if(0<b)for(var e=!0,f=0,g=0,l=0,k=d[l]=0;k<a;k+=c)d[l]+=c,e?f+=c:g+=c,e==f/(f+g)>b&&(l++,d[l]=0,e=!e);return d},sbPlay:function(a){navigator.mozVibrate?(navigator.mozVibrate(0),0<a.length&&navigator.mozVibrate(a)):
navigator.vibrate&&(navigator.vibrate(0),0<a.length&&navigator.vibrate(a))},fnGetText:function(a){if(1>a.length)return"";for(var b=!0,c="",d=0,e=0,f=0,g=a.length;f<g;f++){for(var l=0;l<a[f];l++)c+=b?"|":".",b?d++:e++;b=!b}return c}};var clsBase=clsBase||{};
clsBase={End:null,fnAdjustNumeric:function(a,b){var c=b;void 0!==a&&a.match(/^[+-]?[0-9]*[\.]?[0-9]+$/)&&(c=Number(a));return c},fnConvTable2Propertie:function(a,b,c,d){void 0===d&&(d="");var e=[];a=a.split(b);b=0;for(var f=a.length;b<f;b++){var g=a[b].split(c);e[g[0]]=g[1];e[g[0]]="num"==d?Number(e[g[0]]):e[g[0]]}return e},fnSplit2:function(a,b,c){var d=[];a=a.split(b);b=0;for(var e=a.length;b<e;b++)d[b]=a[b].split(c);return d}};var clsGene=clsGene||{};
clsGene={End:null,fnLenB:function(a){for(var b=0,c=0,d=a.length;c<d;c++){var e=a.charCodeAt(c);b=0<=e&&129>e||63728==e||65377<=e&&65440>e||63729<=e&&63732>e?b+1:b+2}return b},fnGetAllocation:function(a,b,c){var d=[];1>=c?d[0]=[b]:clsGene.fnGetAllocationLoop(d,a,b,c,0);a=[];b=0;for(var e=d.length;b<e;b++)d[b].length==c&&(a[a.length]=d[b]);return a},fnGetAllocationLoop:function(a,b,c,d,e){if(0==e){var f=b;var g=c-d+1}else if(e<d-1){f=b;g=c-(d-e)+(2-b);for(var l=0;l<e;l++)g-=a[a.length-1][l]}else{f=
c;for(l=0;l<d-1;l++)f-=a[a.length-1][l];g=f}for(l=f;l<=g;l++){f=a.length;a[f]=[];for(var k=0;k<e;k++)a[f][k]=a[f-1][k];a[f][e]=l;e<d-1&&clsGene.fnGetAllocationLoop(a,b,c,d,e+1)}return a},fnGetAdjustWidth:function(a,b,c,d,e,f){for(var g=0,l=[],k=0,h=d.length;k<h;k++){g=d[k].length;l[k]=[];for(var n=0;n<g;n++)l[k][n]=clsGene.fnLenB(d[k][n])}d=clsGene.fnGetAllocation(1,10,g);g=0;for(k=d.length;g<k;g++)for(h=0,n=d[g].length;h<n;h++)d[g][h]/=10;h="";g=0;for(k=d.length;g<k;g++)if(n=clsGene.fnGetAdjustWidthLoop(a,
b,c,d[g],l,e,f),void 0===p||n<p){var p=n;h=d[g].join("\t")}return h.split("\t")},fnGetAdjustWidthLoop:function(a,b,c,d,e,f,g){for(var l=d.length,k=[],h=0;h<l;h++){var n=(a-b*(l-1))*Number(d[h]);n-=2*c;k[h]=n/(f/2);--k[h];k[h]=Math.floor(k[h]);k[h]=1>k[h]?1:k[h]}for(b=a=0;b<e.length;b++)for(h=0;h<e[b].length;h++)c=e[b][h]/k[h],1<=c&&(a+=1E3*Math.floor(c),c>=g&&(a+=1E4)),a+=(1-c%1)*k[h];return a},fnJoinInnerCsv:function(a,b,c,d,e,f,g,l){void 0===b&&(b="[");void 0===c&&(c="]");void 0===d&&(d="|");void 0===
e&&(e=",");void 0===f&&(f="");void 0===g&&(g="");void 0===l&&(l="");var k=b,h=c,n=d;"["==k&&(k="\\[");"]"==h&&(h="\\]");"("==k&&(k="\\(");")"==h&&(h="\\)");"|"==n&&(n="|");if(0>a.indexOf(b))return a;for(var p="",m="",r="",t="",q="",u=0,A=0,v=0;v<a.length;v++){var w=a.substr(v,1);0==u?w==e?(p+=(""==p?"":e)+m,m=""):w==b?u=1:m+=w:1==u?w==c?u=2:r+=w:2==u?w==e?u=3:t+=w:q+=w;2<=u&&(0==A?w==b&&(A=1):1==A&&w==c&&(A=2))}a=(r+d+"-").split(n);n=a.length;if(""==l)for(w="",r=0;r<n-1;r++)u=a[r],w+=(""==w?"":e)+
m+u+t;else{v=[];w=[];for(r=0;r<n-1;r++){u=a[r];var z=u.length;void 0===v[z]&&(v[z]="");void 0===w[z+"_"+u]&&(v[z]+=(""==v[z]?"":l)+u);w[z+"_"+u]=1}w="";for(strKey in v)strValue=v[strKey],w+=(""==w?"":e)+m+f+strValue+g+t}w=(""==p?"":p+e)+w+(""==q?"":e+q);2==A&&(w=clsGene.fnJoinInnerCsv(w,b,c,d,e,f,g,l));w=w.replace(new RegExp(k,"g"),"");return w=w.replace(new RegExp(h,"g"),"")}};
```
---
## main_u3d.js
**Path:** `main_u3d.js`

```javascript
window.onload=sbOnloadWait;function sbOnloadWait(){sbOrigOnload();clsCommonMain.sbOnloadCount();clsCommonMain.sbOnloadSocial();clsCommonMain.sbOnloadAma(document.getElementById("txtAmaUrl").value,document.getElementById("txtAmaTag").value,document.getElementById("txtAmaCate").value,document.getElementById("txtAmaKey").value,"","elmAma");setTimeout("clsMain.sbOnload()",100)}
var clsMain=clsMain||{},clsMain={sbShowDescStart4View:function(a){var b=clsCommonMain.fnGetWait();0==a&&0<b||1==a&&0==b||setTimeout("clsMain.sbShowDesc4View()",b)},sbShowDesc4View:function(){document.getElementById("elmDescView").style.display="block"},sbShowDescStart4Edit:function(){var a=clsCommonMain.fnGetWait();setTimeout("clsMain.sbShowDesc4Edit()",a)},sbShowDesc4Edit:function(){document.getElementById("elmDescEdit").style.display="block"},sbDebug:function(){document.getElementById("msg").innerHTML=
""+Math.random()},sbOnload:function(){document.getElementById("elmAdult")&&1>clsCommonMain.sbGetAdult()?clsMain.sbInitAdult():clsMain.sbInit()},sbInitAdult:function(){document.getElementById("elmAdult").style.display="block"},sbClickAdultYes:function(){document.getElementById("elmAdult").style.display="none";clsCommonMain.sbSetAdult(1);clsMain.sbInit()},sbClickAdultNo:function(){document.getElementById("elmAdult").style.display="none"},sbSend:function(){var a,b=document.getElementById("txtName0");
a=document.getElementById("txtName1");var c=document.getElementById("txtName2"),l=document.getElementById("txtName3");a=""==b.value&&""==a.value&&""==c.value&&""==l.value;b.style.backgroundColor=a?"#ff8888":"#ffffff";a?b.focus():clsParam.sbSendForm("")},sbInit:function(){clsParam.sbInit(document,"txtName");clsParam.sbParam2Form("");clsAnime.aiP0=[];clsAnime.aiP1=[];clsAnime.aiP2=[];clsAnime.aiP3=[];clsAnime.aiP4=[];clsAnime.aiP5=[];clsAnime.aiP6=[];clsAnime.aiP7=[];clsAnime.aiP8=[];clsAnime.aiP9=
[];clsAnime.aiLp=[];clsAnime.aiFp=[];clsAnime.aiLw=[];clsAnime.aiAs=[];clsAnime.astrLc=[];clsAnime.astrFc=[];clsAnime.astrQ0=[];clsAnime.astrQ1=[];clsAnime.astrQ2=[];clsAnime.asPath=[];clsAnime.asOpen=[];clsAnime.asCenter=[];clsAnime.asDraw=[];clsAnime.aiLabel=[];var a,b,c,l,f,d,h,g,p,k,m,t,x,y,z,A,B,C,e=0,E=!1,D=[],D=document.getElementById("txtCsv").value.split("!");a="inkei.net".split("");var w=-20;for(b=a.length-9;b<=a.length-1;b++)w+=a[b].charCodeAt(0);for(var u=0;u<D.length;u++){a=clsShape.iDefP0;
b=clsShape.iDefP1;c=clsShape.iDefP2;l=clsShape.iDefP3;f=clsShape.iDefP4;d=clsShape.iDefP5;h=clsShape.iDefP6;g=clsShape.iDefP7;p=clsShape.iDefP8;k=clsShape.iDefP9;m=100;t=20;x=2;y=8;z="FFFFFF";C=B=A="-";document.getElementById("txtName"+u);var v=D[u],n=!1;if(""!=v)for(v=v.replace(/~+/g,"~"),astrValue=v.split("~"),v=0;v<astrValue.length;v++){var q=astrValue[v].substr(0,w%60+w%76-84),r=astrValue[v].substr(w%60+w%76-84);""!=q&&("p0"==q?(n=!0,a=clsMain.fnSetNumber(r,a)):"p1"==q?(n=!0,b=clsMain.fnSetNumber(r,
b)):"p2"==q?(n=!0,c=clsMain.fnSetNumber(r,c)):"p3"==q?(n=!0,l=clsMain.fnSetNumber(r,l)):"p4"==q?(n=!0,f=clsMain.fnSetNumber(r,f)):"p5"==q?(n=!0,d=clsMain.fnSetNumber(r,d)):"p6"==q?(n=!0,h=clsMain.fnSetNumber(r,h)):"p7"==q?(n=!0,g=clsMain.fnSetNumber(r,g)):"p8"==q?(n=!0,p=clsMain.fnSetNumber(r,p)):"p9"==q?(n=!0,k=clsMain.fnSetNumber(r,k)):"lp"==q?(n=!0,m=clsMain.fnSetNumber(r,m)):"fp"==q?(n=!0,t=clsMain.fnSetNumber(r,t)):"lw"==q?(n=!0,x=clsMain.fnSetNumber(r,x)):"as"==q?(n=!0,y=clsMain.fnSetNumber(r,
y)):"lc"==q?(n=!0,z=r):"fc"==q?n=!0:"q0"==q?(n=!0,A=r):"q1"==q?(n=!0,B=r):"q2"==q&&(n=!0,C=r))}if(0==u||n)clsAnime.aiP0[e]=a,clsAnime.aiP1[e]=b,clsAnime.aiP2[e]=c,clsAnime.aiP3[e]=l,clsAnime.aiP4[e]=f,clsAnime.aiP5[e]=d,clsAnime.aiP6[e]=h,clsAnime.aiP7[e]=g,clsAnime.aiP8[e]=p,clsAnime.aiP9[e]=k,clsAnime.aiLp[e]=m,clsAnime.aiFp[e]=t,clsAnime.aiLw[e]=x,clsAnime.aiAs[e]=y,clsAnime.astrLc[e]=z,clsAnime.astrFc[e]=z,clsAnime.astrQ0[e]=A,clsAnime.astrQ1[e]=B,clsAnime.astrQ2[e]=C,clsAnime.asPath[e]=clsShape.fnGetPath3d(a,
b,c,l,f,d,h,g,p,k),clsAnime.asOpen[e]=clsShape.fnGetPath3d(a,b,c,l,f,d,h,g,p,k,"click"),clsAnime.asCenter[e]=clsMorph.fnGetCenterPath3d(clsAnime.asPath[e]),e+=1;n&&(E=!0)}if(2<=e&&0<=clsAnime.astrQ1[e-1].indexOf("test")){--e;for(u=0;u<e;u++)clsAnime.aiAs[u]=1;clsAnime.iViewInterval=25}clsAnime.iLayerCnt=e;clsAnime.iLayerIdx=clsAnime.iLayerCnt-1;E?(document.getElementById("elmView0").style.display="block",document.getElementById("elmView1").style.display="block",document.getElementById("elmEdit0").style.display=
"block",document.getElementById("elmEdit1").style.display="block",document.getElementById("elmEdit2").style.display="block",clsAnime.sbInit(),clsMain.sbShowDescStart4View(0)):(document.getElementById("elmView0").style.display="none",document.getElementById("elmView1").style.display="none",document.getElementById("elmEdit0").style.display="block",document.getElementById("elmEdit1").style.display="block",document.getElementById("elmEdit2").style.display="block",clsMain.sbShowDescStart4Edit())},fnSetNumber:function(a,
b){var c=b;a.match(/[^0-9|^\-|^\.]/g)||(c=Number(a));return c}},clsAnime=clsAnime||{},clsAnime={iViewPanelMinW:320,iViewPanelMaxW:640,iViewPanelM:0,iViewInterval:50,iViewFrameCnt:0,iViewFrameIdx:0,timViewAnime:null,aiP0:null,aiP1:null,aiP2:null,aiP3:null,aiP4:null,aiP5:null,aiP6:null,aiP7:null,aiP8:null,aiP9:null,aiLp:null,aiFp:null,aiLw:null,aiAs:null,astrLc:null,astrFc:null,astrQ0:null,astrQ1:null,astrQ2:null,asPath:null,asDraw:null,asCenter:null,aiLabel:null,strBc:"111111",strGc:"444444",strMc:"FFFFFF",
strDc:"FFFFFF",iLayerCnt:1,iLayerIdx:0,iViewLayerIdx:-1,iOldAngleX:0,iOldAngleY:0,iOldAngleZ:0,iOldPiston:0,iNewAngleX:0,iNewAngleY:0,iNewAngleZ:0,iNewPiston:0,iNowAngleX:0,iNowAngleY:0,iNowAngleZ:0,iNowPiston:0,iLastDankaiPer:1,bClickEvent:!1,bClickInsert:!1,End:null,sbDrawStage:function(){var a=clsPanel.actxCv.cvbg;a.clearRect(0,0,clsPanel.iW,clsPanel.iH);a.fillStyle="#"+clsAnime.strBc;a.globalAlpha=1;a.fillRect(0,0,clsPanel.iW,clsPanel.iH);a=clsPanel.actxCv.cvbg;if(clsAnime.strBc!=clsAnime.strGc){a.lineWidth=
.5*clsPanel.iPer;a.strokeStyle="#"+clsAnime.strGc;a.globalAlpha=1;for(var b=0;b<=clsShape.iStageWidth/10;b++){var c=Math.floor(clsPanel.iW/(clsShape.iStageWidth/10)*b);a.beginPath();a.moveTo(c,0);a.lineTo(c,clsPanel.iH);a.stroke();a.beginPath();a.moveTo(0,c);a.lineTo(clsPanel.iW,c);a.stroke()}}},sbDrawStageFrame:function(){var a=clsPanel.actxCv.cvbg;if(clsAnime.strBc!=clsAnime.strMc){a.lineWidth=1*clsPanel.iPer;a.strokeStyle="#"+clsAnime.strMc;for(var b=a.globalAlpha=1;64>=b;b+=62){var c=Math.floor(clsPanel.iW/
64*b);a.beginPath();a.moveTo(c,0);a.lineTo(c,clsPanel.iH);a.stroke();a.beginPath();a.moveTo(0,c);a.lineTo(clsPanel.iW,c);a.stroke()}}},sbInit:function(){clsPanel.sbInit("pn0","cvbg,cvst,cvdm",clsAnime.iViewPanelMinW,clsAnime.iViewPanelMinW,clsAnime.iViewPanelMaxW,clsAnime.iViewPanelM);clsAnime.sbDrawStage();var a=clsPanel.iW/64;if(1==clsAnime.iLayerCnt){for(iIdx=0;iIdx<clsAnime.iLayerCnt;iIdx++)clsAnime.aiLabel[2*iIdx+0]=clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,a,a,1,4,0,1,1,2),clsAnime.aiLabel[2*
iIdx+1]=clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,a,a,1,4,0,3,1,1);for(iIdx=0;3>iIdx;iIdx++)clsAnime.aiLabel[iIdx+2]=clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,a,a,3,4,iIdx,0,1,1)}else if(2==clsAnime.iLayerCnt)for(iIdx=0;iIdx<clsAnime.iLayerCnt;iIdx++)clsAnime.aiLabel[2*iIdx+0]=clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,a,a,2,3,iIdx,0,1,2),clsAnime.aiLabel[2*iIdx+1]=clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,a,a,2,3,iIdx,2,1,1);else if(3<=clsAnime.iLayerCnt)for(iIdx=
0;iIdx<clsAnime.iLayerCnt;iIdx++)clsAnime.aiLabel[2*iIdx+0]=clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,a,a,2,6,iIdx%2,3*Math.floor(iIdx/2)+0,1,2),clsAnime.aiLabel[2*iIdx+1]=clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,a,a,2,6,iIdx%2,3*Math.floor(iIdx/2)+2,1,1);for(var b=a=0;b<clsAnime.iLayerCnt;b++)var c=clsMorph.fnGetPerspectiveSize3d(clsPanel.iW,clsAnime.asPath[b],clsShape.iStageWidth),a=a>c?a:c;clsAnime.iPerspective=2*a;document.getElementById("nbst").innerHTML="";document.getElementById("nbdm").innerHTML=
"";document.getElementById("nbev").innerHTML="";clsAnime.timViewAnime=setInterval("clsAnime.sbLoop()",clsAnime.iViewInterval)},sbLoop:function(){var a=!1;clsAnime.iViewFrameIdx>=clsAnime.iViewFrameCnt&&(clsAnime.iViewFrameIdx=0,clsAnime.iViewLayerIdx+=1,clsAnime.iViewLayerIdx>=clsAnime.iLayerCnt&&(a=!0));a?clsAnime.sbEnd():(clsAnime.sbDrawNingen(),clsAnime.iViewFrameIdx+=1)},sbDrawNingen:function(){0==clsAnime.iViewFrameIdx&&(clsAnime.iViewFrameCnt=Math.floor(1E3*clsAnime.aiAs[clsAnime.iViewLayerIdx]/
clsAnime.iViewInterval));var a=(clsAnime.iViewFrameIdx+0)/clsAnime.iViewFrameCnt,b=clsAnime.iViewLayerIdx,c=Math.floor(4*a),a=4*(a+1/clsAnime.iViewFrameCnt-c/4),a=(Math.cos((1-a)*Math.PI)+1)/2,l=a<clsAnime.iLastDankaiPer;clsAnime.iLastDankaiPer=a;var f=[];f.st="";f.dm="";if(c<clsShape.aiAutoX.length-1){var d=clsPanel.actxCv.cvdm;d.clearRect(0,0,clsPanel.iW,clsPanel.iH)}if(0==c){var h=2*a-1;if(0<=h&&1>=h){var d=clsPanel.actxCv[1<=a?"cvbg":"cvdm"],g=clsAnime.aiLabel[2*b+0].iX,p=clsAnime.aiLabel[2*b+
0].iY,k=clsAnime.aiLabel[2*b+0].iW,m=clsAnime.aiLabel[2*b+0].iH*h;d.beginPath();d.rect(g,p,k,m);d.lineWidth=Math.floor(clsAnime.aiLw[b]*clsPanel.iPer);d.strokeStyle="#"+clsAnime.astrLc[b];d.globalAlpha=clsAnime.aiLp[b]/100;d.stroke();g=clsAnime.aiLabel[2*b+1].iX;p=clsAnime.aiLabel[2*b+1].iY;k=clsAnime.aiLabel[2*b+1].iW;m=clsAnime.aiLabel[2*b+1].iH*h;d.beginPath();d.rect(g,p,k,m);d.lineWidth=Math.floor(clsAnime.aiLw[b]*clsPanel.iPer);d.strokeStyle="#"+clsAnime.astrLc[b];d.globalAlpha=clsAnime.aiLp[b]/
100;d.stroke();d.fillStyle="#"+clsAnime.astrFc[b];d.globalAlpha=clsAnime.aiFp[b]/100;d.fill()}}1==clsAnime.iLayerCnt&&3>c&&(h=2*a-1,0<=h&&1>=h&&(g=clsAnime.aiLabel[2+c].iX,p=clsAnime.aiLabel[2+c].iY,k=clsAnime.aiLabel[2+c].iW,m=clsAnime.aiLabel[2+c].iH*h,d=clsPanel.actxCv[1<=a?"cvbg":"cvdm"],d.beginPath(),d.rect(g,p,k,m),d.lineWidth=Math.floor(clsAnime.aiLw[b]*clsPanel.iPer),d.strokeStyle="#"+clsAnime.astrLc[b],d.globalAlpha=clsAnime.aiLp[b]/100,d.stroke(),d.fillStyle="#"+clsAnime.astrFc[b],d.globalAlpha=
clsAnime.aiFp[b]/100,d.fill()));h=1==clsAnime.iLayerCnt&&c==clsShape.aiAutoX.length-2&&1<=a;if(c<clsShape.aiAutoX.length-1){l&&(clsAnime.iOldAngleX=clsShape.aiAutoX[c+0],clsAnime.iOldAngleY=clsShape.aiAutoY[c+0],clsAnime.iOldAngleZ=clsShape.aiAutoZ[c+0],clsAnime.iNewAngleX=clsShape.aiAutoX[c+1],clsAnime.iNewAngleY=clsShape.aiAutoY[c+1],clsAnime.iNewAngleZ=clsShape.aiAutoZ[c+1]);var l=1,t=clsAnime.astrLc[b];0==c&&(l=-a,t=clsMorph.fnGetMorphColor("ffffff",t,a));clsAnime.iNowAngleX=clsAnime.iOldAngleX+
(clsAnime.iNewAngleX-clsAnime.iOldAngleX)*a;clsAnime.iNowAngleY=clsAnime.iOldAngleY+(clsAnime.iNewAngleY-clsAnime.iOldAngleY)*a;clsAnime.iNowAngleZ=clsAnime.iOldAngleZ+(clsAnime.iNewAngleZ-clsAnime.iOldAngleZ)*a;k=clsAnime.aiLabel[2*b+0].iW;m=clsAnime.aiLabel[2*b+0].iH;g=clsAnime.aiLabel[2*b+0].iX;p=clsAnime.aiLabel[2*b+0].iY;d=clsPanel.actxCv[3==c&&1<=a?"cvst":"cvdm"];g=clsMorph.fnGetXY3dOnly(k>m?k:m,clsAnime.asPath[b],clsShape.iStageWidth,clsAnime.iPerspective,g+.5*k,p+.5*m,clsAnime.asCenter[b].iX,
clsAnime.asCenter[b].iY,clsAnime.asCenter[b].iZ,clsAnime.iNowAngleX,clsAnime.iNowAngleY,clsAnime.iNowAngleZ,l,"c");clsMorph.sbDrawPanelBezierCurve(d,clsPanel.iPer,g,clsAnime.aiLw[b],t,.01*clsAnime.aiLp[b]);1==clsAnime.iLayerCnt&&2>=c&&1<=a&&(k=clsAnime.aiLabel[2+c].iW,m=clsAnime.aiLabel[2+c].iH,g=clsAnime.aiLabel[2+c].iX,p=clsAnime.aiLabel[2+c].iY,d=clsPanel.actxCv.cvbg,g=clsMorph.fnGetXY3dOnly(k,clsAnime.asPath[b],clsShape.iStageWidth,clsAnime.iPerspective,g+.5*k,p+.5*m,clsAnime.asCenter[b].iX,clsAnime.asCenter[b].iY,
clsAnime.asCenter[b].iZ,clsAnime.iNowAngleX,clsAnime.iNowAngleY,clsAnime.iNowAngleZ,l),clsMorph.sbDrawPanelBezierCurve(d,clsPanel.iPer,g,clsAnime.aiLw[b],t,.01*clsAnime.aiLp[b]))}h&&(g=document.getElementById("txtLang").value,1==clsAnime.iLayerCnt&&(d=clsShape.fnGetDescList(g,clsAnime.aiP0[0],clsAnime.aiP1[0],clsAnime.aiP2[0],clsAnime.aiP3[0],clsAnime.aiP4[0],clsAnime.aiP5[0],clsAnime.aiP6[0],clsAnime.aiP7[0],clsAnime.aiP8[0],clsAnime.aiP9[0]),k=clsAnime.aiLabel[0].iW,m=clsAnime.aiLabel[0].iH,g=clsAnime.aiLabel[0].iX,
p=clsAnime.aiLabel[0].iY+.4*m,h=clsPanel.iW/64,f.st+=clsPanel.fnGetTableText(g+h,p+h,k-2*h,.6*m-2*h,"r",Math.floor(14*clsPanel.iPer),"#"+clsAnime.strDc,d)));3==c&&1<=a&&(g=clsAnime.aiLabel[2*b+1].iX,p=clsAnime.aiLabel[2*b+1].iY,k=clsAnime.aiLabel[2*b+1].iW,m=clsAnime.aiLabel[2*b+1].iH,h=.015625*clsPanel.iW,l=Math.floor((2>=clsAnime.iLayerCnt?22:16)*clsPanel.iPer),t=Math.floor((2>=clsAnime.iLayerCnt?22:16)*clsPanel.iPer),d="",3<=c&&(d+='<span style="font-size: '+t+'px;">'+clsAnime.astrQ0[b]+"<br /></span>"),
3<=c&&(d+=clsAnime.astrQ1[b]+"<br />"),3<=c&&(d+='<span style="font-size: '+t+'px;">'+clsAnime.astrQ2[b]+"<br /></span>"),f[1<=a?"st":"dm"]+=clsPanel.fnGetTableText(g+h,p,k-2*h,m,"l",l,clsAnime.strDc,d));""!=f.dm&&(document.getElementById("nbdm").innerHTML+=f.dm);""!=f.st&&(document.getElementById("nbst").innerHTML+=f.st)},sbEnd:function(){clsAnime.sbDrawStageFrame();clearInterval(clsAnime.timViewAnime);clsMain.sbShowDescStart4View(1);var a="";for(iRow=0;8>iRow;iRow++)for(iCol=0;6>iCol;iCol++)var b=
clsMorph.fnGetLayoutXY(0,0,clsPanel.iW,clsPanel.iH,0,0,6,8,iCol,iRow,1,1),a=a+clsPanel.fnGetTableText(b.iX,b.iY,b.iW,b.iH,"c",b.iH,"ffffff","&nbsp;&nbsp;","cursor: pointer;",'onclick="clsAnime.sbClick('+iCol+","+iRow+');"');document.getElementById("nbev").innerHTML=a},sbClick:function(a,b){clsAnime.bClickEvent&&(clsAnime.bClickEvent=!1,clearInterval(clsAnime.timViewAnime));clsAnime.iOldAngleX=(clsAnime.iNowAngleX+3600)%360;clsAnime.iOldAngleY=(clsAnime.iNowAngleY+3600)%360;clsAnime.iOldAngleZ=(clsAnime.iNowAngleZ+
3600)%360;clsAnime.iOldPiston=clsAnime.iNowPiston;var c=0,l=-1,f=0,d=0;if(!(2!=a&&3!=a||3!=b&&4!=b))l=clsAnime.bClickInsert?0:1,clsAnime.bClickInsert=!clsAnime.bClickInsert;else if(1!=clsAnime.iLayerCnt||0!=b&&1!=b)0==b?f=-4:1==b?f=-2:2==b?f=-1:5==b?f=1:6==b?f=2:7==b&&(f=4),0==a?d=-2:1==a?d=-1:4==a?d=1:5==a&&(d=2);else if(0==a||1==a)c=1;else if(2==a||3==a)c=2;else if(4==a||5==a)c=3;clsAnime.iNewAngleX=clsAnime.iOldAngleX+45*f;clsAnime.iNewAngleY=clsAnime.iOldAngleY+45*d;clsAnime.iNewAngleZ=clsAnime.iOldAngleZ+
0;1<=c&&3>=c&&(clsAnime.iNewAngleX=(clsShape.aiAutoX[c]+3600)%360,clsAnime.iNewAngleY=(clsShape.aiAutoY[c]+3600)%360,clsAnime.iNewAngleZ=(clsShape.aiAutoZ[c]+3600)%360,180<clsAnime.iOldAngleX-clsAnime.iNewAngleX&&(clsAnime.iNewAngleX+=360),180<clsAnime.iOldAngleY-clsAnime.iNewAngleY&&(clsAnime.iNewAngleY+=360),180<clsAnime.iOldAngleZ-clsAnime.iNewAngleZ&&(clsAnime.iNewAngleZ+=360),180<clsAnime.iNewAngleX-clsAnime.iOldAngleX&&(clsAnime.iNewAngleX-=360),180<clsAnime.iNewAngleY-clsAnime.iOldAngleY&&
(clsAnime.iNewAngleY-=360),180<clsAnime.iNewAngleZ-clsAnime.iOldAngleZ&&(clsAnime.iNewAngleZ-=360));0<=l&&(clsAnime.iNewPiston=l);clsAnime.iViewFrameIdx=0;clsAnime.iViewFrameCnt=Math.floor(1E3*clsAnime.aiAs[0]/clsAnime.iViewInterval/4);clsAnime.timViewAnime=setInterval("clsAnime.sbClickLoop()",clsAnime.iViewInterval);clsPanel.actxCv.cvst.clearRect(0,0,clsPanel.iW,clsPanel.iH);clsAnime.bClickEvent=!0},sbClickLoop:function(){var a=!1;clsAnime.iViewFrameIdx>=clsAnime.iViewFrameCnt&&(a=!0);a?clsAnime.sbClickEnd():
(clsAnime.sbClickDrawNingen(),clsAnime.iViewFrameIdx+=1)},sbClickDrawNingen:function(){var a=(clsAnime.iViewFrameIdx+1)/clsAnime.iViewFrameCnt,a=(Math.cos((1-a)*Math.PI)+1)/2;clsAnime.iNowAngleX=clsAnime.iOldAngleX+(clsAnime.iNewAngleX-clsAnime.iOldAngleX)*a;clsAnime.iNowAngleY=clsAnime.iOldAngleY+(clsAnime.iNewAngleY-clsAnime.iOldAngleY)*a;clsAnime.iNowAngleZ=clsAnime.iOldAngleZ+(clsAnime.iNewAngleZ-clsAnime.iOldAngleZ)*a;clsAnime.iNowPiston=clsAnime.iOldPiston+(clsAnime.iNewPiston-clsAnime.iOldPiston)*
a;a=clsPanel.actxCv.cvdm;a.clearRect(0,0,clsPanel.iW,clsPanel.iH);for(iLayerIdx=0;iLayerIdx<clsAnime.iLayerCnt;iLayerIdx++){var b=clsAnime.aiLabel[2*iLayerIdx+0].iW,c=clsAnime.aiLabel[2*iLayerIdx+0].iH,l=clsAnime.aiLabel[2*iLayerIdx+0].iX,f=clsAnime.aiLabel[2*iLayerIdx+0].iY,d=clsShape.fnMorphDemo3d(clsAnime.asPath[iLayerIdx],clsAnime.asOpen[iLayerIdx],clsAnime.iNowPiston),b=clsMorph.fnGetXY3dOnly(b>c?b:c,d,clsShape.iStageWidth,clsAnime.iPerspective,l+.5*b,f+.5*c,clsAnime.asCenter[iLayerIdx].iX,clsAnime.asCenter[iLayerIdx].iY,
clsAnime.asCenter[iLayerIdx].iZ,clsAnime.iNowAngleX,clsAnime.iNowAngleY,clsAnime.iNowAngleZ,1);clsMorph.sbDrawPanelBezierCurve(a,clsPanel.iPer,b,clsAnime.aiLw[iLayerIdx],clsAnime.astrLc[iLayerIdx],.01*clsAnime.aiLp[iLayerIdx])}},sbClickEnd:function(){clsAnime.bClickEvent=!1;clearInterval(clsAnime.timViewAnime)}};
```
---
## orig_inkei.css
**Path:** `orig_inkei.css`

```css
body#bdyu div.head,body#bdyu div#elmBnnr2 { background-image: url(//inkei.net/common/images/inkei/page_head_u.png); }
body#bdyd div.head,body#bdyd div#elmBnnr2 { background-image: url(//inkei.net/common/images/inkei/page_head_d.png); }
body#bdyb div.head,body#bdyb div#elmBnnr2 { background-image: url(//inkei.net/common/images/inkei/page_head_b.png); }

body#bdyu div.fm td    { background-image: url(//inkei.net/common/images/inkei/page_head_u.png); background-color: #6c5d53; border-color: #eeeeee; }
body#bdyd div.fm td    { background-color: #5d6c53; border-color: #eeeeee; }
body#bdyb div.fm td    { background-color: #008000; border-color: #eeeeee; }

body#bdyu *      { border-color: #6c5d53; }
body#bdyd *      { border-color: #5d6c53; }
body#bdyb *      { border-color: #008000; }

body#bdyu a      { color: #883333; }
body#bdyd a      { color: #338833; }
body#bdyb a      { color: #338833; }

ul li            { background-image: url(//inkei.net/common/images/inkei/page_li.png); }
div.info ul li   { background-image: url(//inkei.net/common/images/inkei/page_li_info.png); }
.ddvl            { background-image: url(//inkei.net/common/images/inkei/page_dd_slider.png?5); }
div.info         { color: #857970; }

div#elmP7        { display: none; }
div#elmP8        { display: none; }
div#elmP9        { display: none; }
body#bdyd table#elmTableP7 { display: none; }
body#bdyd table#elmTableP8 { display: none; }
body#bdyd table#elmTableP9 { display: none; }
```
---
## orig_inkei.js
**Path:** `orig_inkei.js`

```javascript
// --------------------------------------------------------------------------------
//	1文字目：部位
//	a	All	全体
//	b	Back	背景
//	f	Fill	塗り
//	g	Grid	グリッド
//	h	Head	亀頭
//	l	Line	線
//	m	aniMe	アニメ
//	q	-	その他
//	r	Root	根本
//	s	Stem	茎
//	t	poinT	点
//	2文字目：属性
//	a	Angle	角度
//	c	Color	色
//	d	Distance	距離感覚
//	e	Expansion rate	膨張率
//	f	circumFerence	外周
//	h	Height	高さ（未使用）
//	l	Length	長さ
//	p	Permeation rate	濃度
//	r	Radius	半径
//	s	Sec	変形時間
//	v	curVe	カーブ
//	w	Width	太さ
//	x	X	X座標
//	y	Y	Y座標
var clsShapeInkei = clsShapeInkei || {};
clsShapeInkei = {
//20140327
	iMainSt : 0,
	iMainEd : 24,
//	iMainSt : 3,
//	iMainEd : 27,
//20140327
	iDefAx : -150,
	iDefAy : 0,
	iDefAa : 0,
	iMinP0 : 50,	iMaxP0 : 300,	iIvlP0 : 1,	iDefP0 : 140,
	iMinP1 : 50,	iMaxP1 : 300,	iIvlP1 : 1,	iDefP1 : 140,
	iMinP2 : -60,	iMaxP2 : 60,	iIvlP2 : 1,	iDefP2 : 10,
	iMinP3 : -60,	iMaxP3 : 60,	iIvlP3 : 1,	iDefP3 : 10,
	iMinP4 : -40,	iMaxP4 : 40,	iIvlP4 : 1,	iDefP4 : 0,
	iMinP5 : 75,	iMaxP5 : 200,	iIvlP5 : 1,	iDefP5 : 100,
	iMinP6 : 75,	iMaxP6 : 150,	iIvlP6 : 1,	iDefP6 : 100,
	iMinP7 : 0,	iMaxP7 : 1,	iIvlP7 : 1,	iDefP7 : 0,
	iMinP8 : 0,	iMaxP8 : 1,	iIvlP8 : 1,	iDefP8 : 0,
	iMinP9 : 0,	iMaxP9 : 1,	iIvlP9 : 1,	iDefP9 : 0,
	
//20140426
	bJohan : true,
//20140426
//20140404
	bOption0 : true,
	bOption1 : true,
//20140404
	
//20140327
	I_KUKI0 : 0,
	I_KUKI1 : 3,
	I_KITO0 : 6,
	I_KITO1 : 9,
	I_RINKO : 12,
	I_KITO2 : 15,
	I_KITO3 : 18,
	I_KUKI2 : 21,
	I_KUKI3 : 24,
//	I_KUKI0 : 3,
//	I_KUKI1 : 6,
//	I_KITO0 : 9,
//	I_KITO1 : 12,
//	I_RINKO : 15,
//	I_KITO2 : 18,
//	I_KITO3 : 21,
//	I_KUKI2 : 24,
//	I_KUKI3 : 27,
//20140327
	
//20140705
	iStageWidth : 320,
	aiAutoX : [    0,    0,    0,   90,    0],
	aiAutoY : [ -160,  -90,  180,  360,  630],
	aiAutoZ : [    0,    0,    0,    0,    0],
//20140705
	
	iEnd : 0
};

clsShapeInkei.fnGetFny0 = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath( 90, 80,-20,-40,-30,140, 80,iP7,iP8,iP9);
}

clsShapeInkei.fnGetFny1 = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath(iP0, 80,  0,  0,  0,iP5,iP6,iP7,iP8,iP9);
}

clsShapeInkei.fnGetFny2 = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath(iP0,iP1,  0,  0,  0,iP5,iP6,iP7,iP8,iP9);
}

clsShapeInkei.fnGetGtai = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	return clsShapeInkei.fnGetPath(iP0,iP1,  0,  0,iP4,iP5,iP6,iP7,iP8,iP9);
}

clsShapeInkei.fnGetPath = function(iAl,iRf,iSv,iSa,iHa,iSe,iHe,iP7,iP8,iP9) {
	// 定数
//20140327
	var aiX = [0,29,55,84,86,89,91,92,93,96,105,124,129,128,123,116,113,113,111,109,106,103,66,34,0];
	var aiY = [0,2,3,1,2,2,4,2,0,-3,0,1,13,21,29,32,31,31,30,31,32,33,36,35,35];
//	var aiX = [-160,82.32,-33.22,0,29.24,55.29,84.23,86.14,88.79,90.83,91.56,93.48,96.08,105.1,123.52,128.64,128.11,123.26,116.28,113.42,112.51,111.04,109.18,106.4,103.03,66.2,33.87,0,-13.97,24.05,-9.15,-21.98,1.09,-160];
//	var aiY = [-465,-465,-167.9,0,1.39,2.67,0.85,1.32,1.66,3.37,1.24,-0.63,-3.02,-0.56,0.97,12.49,20.36,28.93,31.64,31.03,30.43,29.82,30.51,32.01,33.07,35.89,34.74,35,59.16,77.44,95.25,234.19,496.38,495];
//20140327
	
	var KUKI0 = clsShapeInkei.I_KUKI0;
	var KUKI1 = clsShapeInkei.I_KUKI1;
	var KITO0 = clsShapeInkei.I_KITO0;
	var KITO1 = clsShapeInkei.I_KITO1;
	var RINKO = clsShapeInkei.I_RINKO;
	var KITO2 = clsShapeInkei.I_KITO2;
	var KITO3 = clsShapeInkei.I_KITO3;
	var KUKI2 = clsShapeInkei.I_KUKI2;
	var KUKI3 = clsShapeInkei.I_KUKI3;
	
	// 汎用変数
	var iIdx;
	var iPr;
	var iX;
	var iY;
	var iW;
	var iH;
	var iR;
	var iS;
	var astrTemp = [];
	
	// ----------------------------------------
	// 外周から直径を求める
	var iChokei = iRf / Math.PI;
	
	// 拡大すべき縦幅の倍率を求める
	iPr = (iChokei / (aiY[KUKI3] - aiY[KUKI0]));
	
	// 直径の分だけ縦幅を拡大
	for (iIdx = 0; iIdx < aiX.length; iIdx++) {
		aiY[iIdx] = aiY[iIdx] * iPr;
	}
	
	// 縦幅が拡大した分だけ亀頭の横幅を拡大するが、サオと亀頭の境目のくびれる直前部分がマイナスになる場合は倍率を変更
	if (aiX[RINKO] + (aiX[KUKI1] - aiX[RINKO]) * iPr < aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 0.1) {
		iPr = (aiX[KUKI0] + (aiX[RINKO] - aiX[KUKI0]) * 1) / (aiX[RINKO] - aiX[KUKI1]);
	}
	
	// 縦幅が拡大した分だけ亀頭の横幅を拡大する
	for (iIdx = KUKI1; iIdx <= KUKI2; iIdx++) {
		aiX[iIdx] = aiX[RINKO] + (aiX[iIdx] - aiX[RINKO]) * iPr;
	}
	
	// ----------------------------------------
	// サオと亀頭の境目のくびれた直後部分の中心座標Aを求める
	var iX = aiX[KITO0] + (aiX[KITO3] - aiX[KITO0]) * 0.5;
	var iY = aiY[KITO0] + (aiY[KITO3] - aiY[KITO0]) * 0.5;
	
	// 亀頭の縦幅を拡大
	for (iIdx = KITO1 - 1; iIdx <= KITO2 + 1; iIdx++) {
		aiX[iIdx] = iX + (aiX[iIdx] - iX) * (iHe / 100);
		aiY[iIdx] = iY + (aiY[iIdx] - iY) * (iHe / 100);
	}
	
	// ----------------------------------------
	// サオの対角線部分の中心座標Aを求める
	var iX = aiX[KUKI0] + (aiX[KUKI2] - aiX[KUKI0]) * 0.5;
	var iY = aiY[KUKI0] + (aiY[KUKI2] - aiY[KUKI0]) * 0.5;
	
	// サオの縦幅を拡大
	for (iIdx = KUKI0 + 1; iIdx <= KUKI3 - 1; iIdx++) {
		if (iIdx <= KUKI1 - 1 || iIdx >= KUKI2 + 1) {
			aiX[iIdx] = iX + (aiX[iIdx] - iX) * (iSe / 100);
			aiY[iIdx] = iY + (aiY[iIdx] - iY) * (iSe / 100);
		}
	}
	
	// ----------------------------------------
	// 拡大すべき横幅の倍率を求める
	iPr = (iAl / (aiX[RINKO] - aiX[KUKI0]));
	
	// 先端部分のX座標を求める
	iX = aiX[RINKO] * iPr;
	
	// 先端部分の伸び幅を求める
	iW = iX - aiX[RINKO];
	
	// 伸び幅の分だけ亀頭を移動
	for (iIdx = KUKI1; iIdx <= KUKI2; iIdx++) {
		aiX[iIdx] += iW;
	}
	
	// サオの制御点を補正
	for (iIdx = 1; iIdx <= 2; iIdx++) {
		aiX[KUKI0 + iIdx] = aiX[KUKI0] + (aiX[KUKI1] - aiX[KUKI0]) * iIdx / 3;
		aiX[KUKI3 - iIdx] = aiX[KUKI3] + (aiX[KUKI2] - aiX[KUKI3]) * iIdx / 3;
	}
	
	// ----------------------------------------
	// サオの上辺の中心座標Aを求める
	var iX = aiX[KUKI0 + 1] + (aiX[KUKI0 + 2] - aiX[KUKI0 + 1]) * 0.5;
	var iY = aiY[KUKI0 + 1] + (aiY[KUKI0 + 2] - aiY[KUKI0 + 1]) * 0.5;
	
	// 始点から座標Aの半径を求める
	iR = Math.sqrt(Math.pow(iX,2) + Math.pow(iY,2));
	
	// 始点から座標Aの角度を求める
	iS = (Math.atan2(iY,iX) / (Math.PI / 180));
	
	// 角度を変更
	iS -= iSv;
	
	// Yの移動量を求める
	iH = iY - (Math.sin(iS / 180 * Math.PI) * iR);
	
	// 反り
	for (iIdx = KUKI0 + 1; iIdx <= KUKI3 - 1; iIdx++) {
		if (iIdx <= KUKI1 - 1 || iIdx >= KUKI2 + 1) {
			aiY[iIdx] += iH;
		}
	}
	
	// 反った分だけ始点と終点の縦幅を拡大
	var iSvStEdHPer = (1 / Math.cos(iSv / 180 * Math.PI));
	iSvStEdHPer = (iSvStEdHPer - 1) * 0.5 + 1;
	aiY[KUKI0] *= iSvStEdHPer;
	aiY[KUKI3] *= iSvStEdHPer;
	
	// ----------------------------------------
	// サオと亀頭の境目のくびれる直前部分の中心座標Aを求める
	var iX = aiX[KUKI1] + (aiX[KUKI2] - aiX[KUKI1]) * 0.5;
	var iY = aiY[KUKI1] + (aiY[KUKI2] - aiY[KUKI1]) * 0.5;
	
	// 反りの分だけ回転
	for (iIdx = KUKI1; iIdx <= KUKI2; iIdx++) {
		astrTemp = clsShapeInkei.fnRotate(iX,iY,aiX[iIdx],aiY[iIdx],-iSv);
		aiX[iIdx] = astrTemp.iX;
		aiY[iIdx] = astrTemp.iY;
	}
	
	// ----------------------------------------
	// 支点を求める
	var iX = aiX[KUKI0];
	var iY = aiY[KUKI0];
	
	// サオ角度の分だけ回転
	for (iIdx = KUKI0 + 1; iIdx <= KUKI3 - 1; iIdx++) {
		astrTemp = clsShapeInkei.fnRotate(iX,iY,aiX[iIdx],aiY[iIdx],-iSa);
		aiX[iIdx] = astrTemp.iX;
		aiY[iIdx] = astrTemp.iY;
	}
	
	// 曲げた分だけ始点と終点の縦幅を拡大
	var iSaStEdHPer = (1 / Math.cos(iSa / 180 * Math.PI));
	aiY[KUKI0] *= iSaStEdHPer;
	aiY[KUKI3] *= iSaStEdHPer;
	
	// ----------------------------------------
	// サオと亀頭の境目のくびれた直後部分の中心座標Aを求める
	var iX = aiX[KITO1] + (aiX[KITO2] - aiX[KITO1]) * 0.5;
	var iY = aiY[KITO1] + (aiY[KITO2] - aiY[KITO1]) * 0.5;
	
	// 亀頭角度の分だけ回転
	for (iIdx = RINKO - 1; iIdx <= RINKO + 1; iIdx++) {
		astrTemp = clsShapeInkei.fnRotate(iX,iY,aiX[iIdx],aiY[iIdx],-iHa);
		aiX[iIdx] = astrTemp.iX;
		aiY[iIdx] = astrTemp.iY;
	}
	
	// ----------------------------------------
	// 始点と終点の縦幅を求める
	iH = aiY[KUKI3] - aiY[KUKI0];
	
	// 始点が支点の位置で低すぎるため全ての座標を縦幅の半分だけ上に移動する
	for (iIdx = 0; iIdx < aiX.length; iIdx++) {
		aiY[iIdx] -= iH * 0.5;
	}
	
//20140327
//	// Xにマイナスのものがあれば0にする
//	for (iIdx = 0; iIdx < aiX.length; iIdx++) {
//		aiX[iIdx] = aiX[iIdx] < 0 ? 0 : aiX[iIdx];
//	}
//20140327
	
	// ----------------------------------------
	
	return { aiX: aiX, aiY: aiY };
}

clsShapeInkei.fnRotate = function(iBaseX,iBaseY,iX,iY,iAngle) {
	if (iAngle % 360 != 0) {
		// 始点からの半径を求める
		var iR = Math.sqrt(Math.pow(iX - iBaseX,2) + Math.pow(iY - iBaseY,2));
		
		// 始点からの角度を求める
		var iS = (Math.atan2(iY - iBaseY,iX - iBaseX) / (Math.PI / 180));
		
		// 角度を変更
		iS += iAngle;
		
		// 各座標に適用
		iX = iBaseX + Math.cos(iS / 180 * Math.PI) * iR;
		iY = iBaseY + Math.sin(iS / 180 * Math.PI) * iR;
	}
	
	return { iX : iX, iY : iY };
}

clsShapeInkei.fnGetDescList = function(strLang,iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9) {
	var strText = '';
	strText += 'Length : ' + iP0 + 'mm<br />';
	strText += 'Diameter : &phi;' + Math.floor(iP1 / Math.PI) + 'mm<br />';
	strText += 'Shaft Curve : ' + iP2 + '&deg;<br />';
	strText += 'Shaft Angle : ' + iP3 + '&deg;<br />';
	strText += 'Glans Angle : ' + iP4 + '&deg;<br />';
	strText += 'Shaft Expansion rate : ' + iP5 + '%<br />';
	strText += 'Glans Expansion rate : ' + iP6 + '%<br />';
	return strText;
}

clsShapeInkei.fnGetDescArray = function(strLang,iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9,asDraw,iW,iH,bDetail) {
	var KUKI0 = clsShapeInkei.I_KUKI0;
	
	var aiX = [];
	var aiY = [];
	var astrText = [];
	var iIdx = -1;
	
	if (bDetail) {
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 11]; aiY[iIdx] = asDraw.aiY[KUKI0 + 11]; astrText[iIdx] = iP0 + 'mm';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 24]; aiY[iIdx] = asDraw.aiY[KUKI0 + 24]; astrText[iIdx] = '&phi;' + Math.floor(iP1 / Math.PI) + 'mm';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 +  1]; aiY[iIdx] = asDraw.aiY[KUKI0 +  3]; astrText[iIdx] = iP2 + '&deg;';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 +  0]; aiY[iIdx] = asDraw.aiY[KUKI0 +  0]; astrText[iIdx] = iP3 + '&deg;';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 13]; aiY[iIdx] = asDraw.aiY[KUKI0 + 13]; astrText[iIdx] = iP4 + '&deg;';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 +  9]; aiY[iIdx] = asDraw.aiY[KUKI0 +  9]; astrText[iIdx] = iP5 + '%';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 23]; aiY[iIdx] = asDraw.aiY[KUKI0 + 23]; astrText[iIdx] = iP6 + '%';
	} else {
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 12]; aiY[iIdx] = asDraw.aiY[KUKI0 + 12]; astrText[iIdx] = iP0 + 'mm';
		iIdx++; aiX[iIdx] = asDraw.aiX[KUKI0 + 1] + (asDraw.aiX[KUKI0 + 23] - asDraw.aiX[KUKI0 + 1]) * 0.5; aiY[iIdx] = asDraw.aiY[KUKI0 + 1] + (asDraw.aiY[KUKI0 + 23] - asDraw.aiY[KUKI0 + 1]) * 0.5; astrText[iIdx] = '&phi;' + Math.floor(iP1 / Math.PI) + 'mm';
	}
	
	return { aiX: aiX, aiY: aiY, astrText: astrText };
}

//20141209
clsShapeInkei.fnConv3d = function(sShape) {
	return clsMorph.fnConvXYtoXYZofCylinder3d(sShape,[clsShapeInkei.iMainSt],[clsShapeInkei.iMainEd],12,[],[0,0]);
}
//20141209

clsShapeInkei.fnGetPath3d = function(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9,strMode) {
	strMode = strMode || '';
	
	var sShape;
	if (strMode == 'click') {
		sShape = clsShapeInkei.fnGetFny0(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9)
	} else {
		sShape = clsShapeInkei.fnGetPath(iP0,iP1,iP2,iP3,iP4,iP5,iP6,iP7,iP8,iP9)
	}
//20141209
//	return clsMorph.fnConvXYtoXYZofCylinder3d(sShape,[0],[24],12,[],[0,0]);
	return clsShapeInkei.fnConv3d(sShape);
//20141209
}

clsShapeInkei.fnMorphDemo3d = function(sShapeSt,sShapeEd,iMorphPer) {
	var sShape = clsMorph.fnGetMophPath3d(sShapeSt,sShapeEd,iMorphPer);
	return sShape;
}

clsShapeInkei.fnOrigMorph3d = function(sShapeSt,sShapeEd,iR) {
}
```
---
## Penis of A - Penis Analyzer.html
**Path:** `Penis of A - Penis Analyzer.html`

```html
<!DOCTYPE html>
<!-- saved from url=(0022)https://en.inkei.net/A -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<!-- analytics -->
<!-- Google tag (gtag.js) -->
<script src="./Penis of A - Penis Analyzer_files/widgets.js.Без названия" async="" id="twitter-wjs"></script><script async="" src="./Penis of A - Penis Analyzer_files/js"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MVBDTBQVWM');
</script>
<!-- analytics -->

		
		<meta name="robots" content="all">
		<meta name="author" content="inkeinet">
		<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no">
		<meta name="keywords" content="Penis,Analyzer,Design,Tool,Inkei,Spec,A">
		<meta name="description" content="The system analyzes the specifications of the penis.">
		<link rel="stylesheet" href="./Penis of A - Penis Analyzer_files/common.css" type="text/css">
		<link rel="stylesheet" href="./Penis of A - Penis Analyzer_files/common_inkei.css" type="text/css">
		<link rel="stylesheet" href="./Penis of A - Penis Analyzer_files/orig_inkei.css" type="text/css">
		<link rel="shortcut icon" type="png" href="https://inkei.net/common/images/inkei/logo_16x16.png">
		<script type="text/javascript" src="./Penis of A - Penis Analyzer_files/jquery-1.11.0.min.js.Без названия"></script>
		<script type="text/javascript" src="./Penis of A - Penis Analyzer_files/jquery.storage.js.Без названия"></script>
		<script type="text/javascript" src="./Penis of A - Penis Analyzer_files/common_0.js.Без названия"></script>
		<script type="text/javascript" src="./Penis of A - Penis Analyzer_files/main_u3d.js.Без названия"></script>
		<script type="text/javascript" src="./Penis of A - Penis Analyzer_files/orig_inkei.js.Без названия"></script>
		<link rel="start" href="https://inkei.net/menu/">
		<meta property="og:type" content="website">
		<meta property="og:url" content="https://inkei.net/menu/">
		<meta property="og:title" content="INKEI.NET">
		<meta property="og:description" content="The system analyzes the specifications of the penis.">
		<meta property="og:image" content="https://inkei.net/menu/index/ogp.png">
		<script>
		var clsShape;
		function sbOrigOnload() {
			clsShape = clsClass.fnCopyClass(clsShapeInkei);
		}
		</script>
		<title>Penis of A - Penis Analyzer</title>
		
	</head>
	<body id="bdyu">
		<div id="elmDescCmmn">
			<p>
			Penis of A<br>
			THE GLITTER APACHE REVOLVER / A's Penis / Ability : 30%<br>
			</p>
		</div>
		<div class="d1">
			<div class="head"><div class="menu"><a href="https://inkei.net/menu/"><img src="./Penis of A - Penis Analyzer_files/page_en_button_menus.png" alt="Service" width="100" height="30"></a></div><img src="./Penis of A - Penis Analyzer_files/logo_en_320x80_u.png" width="320" height="80"></div>
			<div class="main2">
				
				<div id="elmEdit0" style="display: block;">
				</div>
				<div id="elmView0" style="display: block;">
					<div class="ct">
						<div id="pn0" class="pn" style="width: 640px; height: 640px;">
							<canvas id="cvbg" width="640" height="640"></canvas>
							<canvas id="cvst" width="640" height="640"></canvas>
							<canvas id="cvdm" width="640" height="640"></canvas>
							<div id="nbst"><table style="left:30px; top:300px; width:580px;height:156px;"><tbody><tr><td style="font-size:14px; color:#FFFFFF; text-align:right;">Length : 143mm<br>Diameter : φ45mm<br>Shaft Curve : 16°<br>Shaft Angle : 6°<br>Glans Angle : 1°<br>Shaft Expansion rate : 119%<br>Glans Expansion rate : 75%<br></td></tr></tbody></table><table style="left:30px; top:476px; width:580px;height:142px;"><tbody><tr><td style="font-size:22px; color:#FFFFFF; text-align:left;"><span style="font-size: 22px;">THE GLITTER APACHE REVOLVER<br></span>A's Penis<br><span style="font-size: 22px;">Ability : 30%<br></span></td></tr></tbody></table></div>
							<div id="nbdm"></div>
							<div id="nbev"><table style="left:0px; top:0px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,0);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:0px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,0);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:0px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,0);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:0px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,0);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:0px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,0);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:0px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,0);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:0px; top:80px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,1);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:80px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,1);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:80px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,1);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:80px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,1);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:80px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,1);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:80px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,1);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:0px; top:160px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,2);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:160px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,2);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:160px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,2);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:160px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,2);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:160px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,2);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:160px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,2);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:0px; top:240px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,3);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:240px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,3);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:240px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,3);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:240px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,3);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:240px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,3);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:240px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,3);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:0px; top:320px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,4);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:320px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,4);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:320px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,4);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:320px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,4);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:320px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,4);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:320px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,4);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:0px; top:400px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,5);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:400px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,5);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:400px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,5);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:400px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,5);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:400px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,5);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:400px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,5);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:0px; top:480px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,6);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:480px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,6);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:480px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,6);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:480px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,6);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:480px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,6);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:480px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,6);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:0px; top:560px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(0,7);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:106px; top:560px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(1,7);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:212px; top:560px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(2,7);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:318px; top:560px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(3,7);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:424px; top:560px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(4,7);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table><table style="left:530px; top:560px; width:106px;height:80px; cursor: pointer;" onclick="clsAnime.sbClick(5,7);"><tbody><tr><td style="font-size:80px; color:#ffffff; text-align:center;">&nbsp;&nbsp;</td></tr></tbody></table></div>
						</div>
						<p id="msg"></p>
					</div>
				</div>
				<div id="elmView1" style="display: block;">
					
					<ul><li>Please free to use the image.</li><li>You can share the image using the current URL.</li></ul>
					<div id="elmDescView" style="display: block;">
						<div class="ct">
							<img class="btn" alt="Penis of A" src="./Penis of A - Penis Analyzer_files/share_twitter.png" width="32" height="32" onclick="window.open(&#39;https://twitter.com/intent/tweet?text=Penis%20of%20A&amp;url=https%3A%2F%2Fen.inkei.net%2FA&#39;,&#39;tweetwindow&#39;,&#39;width=550, height=450, personalbar=0, toolbar=0, scrollbars=1, resizable=!&#39;); return false;">
							<img class="btn" alt="Penis of A" src="./Penis of A - Penis Analyzer_files/share_facebook.png" width="32" height="32" onclick="window.open(&#39;https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fen.inkei.net%2FA&#39;,&#39;facebook-share-dialog&#39;,&#39;width=626,height=436&#39;); return false;">
							
							
							
							<a href="https://line.me/R/msg/text/?Penis%20of%20A%0D%0Ahttps%3A%2F%2Fen.inkei.net%2FA"><img class="btn" alt="Penis of A" src="./Penis of A - Penis Analyzer_files/share_line.png" width="30" height="30"></a>
						</div>
					</div>
				</div>
				
				<div id="elmEdit1" style="display: block;">
					<p class="release">Feb. 24, 2025 This site has released a Sex Reversi.<a href="https://en.inkei.net/reversi/">URL</a></p>
					<p>The system analyzes the specifications of the penis based on the name.</p>
					<div id="elmDescEdit">
						<ul><li>Enter the name of the male.</li><li>It can also be compared by entering more than one name.</li></ul>
					</div>
				</div>
				
				<div id="elmEdit2" style="display: block;">
					<div class="ct">
						<div class="ddfm">
							<div class="fm">
								        <table><tbody><tr><td><input class="str" id="txtName0" type="text" value="" maxlength="20"></td></tr>
								</tbody></table><table><tbody><tr><td><input class="str" id="txtName1" type="text" value="" maxlength="20"></td></tr>
								</tbody></table><table><tbody><tr><td><input class="str" id="txtName2" type="text" value="" maxlength="20"></td></tr>
								</tbody></table><table><tbody><tr><td><input class="str" id="txtName3" type="text" value="" maxlength="20"></td></tr>
								</tbody></table>
							</div>
						</div>
					</div>
					
					<div class="ct">
						<img class="btn" src="./Penis of A - Penis Analyzer_files/page_en_button_u.png" alt="Analyze" width="120" height="35" onclick="clsMain.sbSend();">
					</div>
					<ul><li>People with the same name exist in the world, but this system shows the average specs of people with the same name.</li><li>There is a version of the 14 languages ​​in this Web site.</li></ul>
					<div class="ct">
						
					</div>
				</div>
				<input id="txtAmaUrl" type="hidden" value="/cgi/ama.cgi">
				<input id="txtAmaTag" type="hidden" value="inkei-22">
				<input id="txtAmaCate" type="hidden" value="All">
				<input id="txtAmaKey" type="hidden" value=",A">
				<input id="txtCsv" type="hidden" value="~p0220~p1143~p216~p36~p41~p5119~p675~lcFF3737~q0THE GLITTER APACHE REVOLVER~q1A&#39;s Penis~q2Ability : 30%">
				<input id="txtLang" type="hidden" value="en">
				<br>
			</div>
			
			<a name="service"></a>
			<div class="foot">
				<div class="footsite"></div>
				<p class="footlang"><a href="https://hi.inkei.net/A">हिन्दी</a> <a href="https://pt.inkei.net/A">Português</a> <a href="https://tr.inkei.net/A">Türkçe</a> <a href="https://it.inkei.net/A">Italiano</a> <a href="https://tw.inkei.net/A">繁體中文</a> <a href="https://es.inkei.net/A">Español</a> <a href="https://ru.inkei.net/A">Русский</a> <a href="https://ar.inkei.net/A">العربية</a> <a href="https://en.inkei.net/A">English</a> <a href="https://fr.inkei.net/A">Français</a> <a href="https://de.inkei.net/A">Deutsch</a> <a href="https://inkei.net/A">日本語</a> <a href="https://vi.inkei.net/A">Việt</a> <a href="https://th.inkei.net/A">ภาษาไทย</a></p>
			</div>
			<div class="main2">
				
				
				<br>
			</div>
			<div class="foot">
				<p class="footcopy">Copyright © <a href="https://twitter.com/inkeinet" target="_blank">inkei.net</a> All Rights Reserved. - 0.019[new]</p>
			</div>
			
		</div>
	

<iframe scrolling="no" frameborder="0" allowtransparency="true" src="./Penis of A - Penis Analyzer_files/widget_iframe.2f70fb173b9000da126c79afe2098f02.html" title="Twitter settings iframe" style="display: none;"></iframe><iframe id="rufous-sandbox" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" style="position: absolute; visibility: hidden; display: none; width: 0px; height: 0px; padding: 0px; border: none;" title="Twitter analytics iframe" src="./Penis of A - Penis Analyzer_files/saved_resource.html"></iframe></body></html>
```
---