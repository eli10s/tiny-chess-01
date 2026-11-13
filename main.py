import json,os,sys
import urllib.request as u
# PROTOCOL (make.fun env, exact per kit): POST /game {} -> state; POST /move
# {"game":n,"move":"e2e4"} -> next state; ends at status "done". Swap only G/M.
URL=os.environ.get("MAKEFUN_ENV_URL","")
def P(p,b):
 q=u.Request(URL+p,json.dumps(b).encode(),{"content-type":"application/json"})
 try:
  with u.urlopen(q)as r:return json.load(r)
 except Exception as e:sys.exit(str(e))
def G():return P("/game",{})
def M(g,m):return P("/move",{"game":g,"move":m})
# ENGINE -- lzma+base85 payload; source: engine_src.py (same code, golfed).
import lzma,base64
exec(lzma.decompress(base64.b85decode('T>t<81poj4|NsC0{{Rt)1tz%{hogYJR*@`6sM))-Kc~DQKG)WdN&xNPjQ=26s8RVL9h7`z%7p6O8X<A%Md0k!kPVkLM<((!`2xc#AR1I9jY^ugB=~+p$Mf|6e!XBh=WMn4;Vh5GBRwwQ?Q_<~)`3z&G6(=TxV<S}OO2--S2M{Rz<tJ@!*^VzR2Un=G47?XePN#Vu1{kVVg`Ld`P!e+QqG1KRnL0>wCME6KYIPOW6)ZNf!s5<TRk9v0cYFEhVy^QW5*FZ%>VmX>c@(sahlx#v>4Mf@L@GJSmZUQvE#mY-(c?XCAH{pLtIm|gd&!UhFllccMNjYp7=M9oEaJgJ$&+}G9Tg!_n8koh)C9Fj%fUP>0}iZj^-k!fUa7#z%|hq`XIBJ%adNn3Xj?XcVjQ2R9tBjEW}5XIYpqmLw6Pl(K)%W)Uh!l4Hh(WoK<)vmZbltI-B)SXWjmlb#xFjT*nxAQof;BLLm#q)U4l-BH)LNY-cq%7+vQV#Fjl`YM4}5b?%~aA$;0*@)m~Z$9&(JL7^3-T$G_3K?+o3)c(I!u0O;DZaTid7eO#qaoFn8$Ufh*I7V~(;ZnNSm#ktVfUo4!<%N|dV4*K07;C1<hH!ASR=4|V>pQrff02nF5!uY+{ER81%wvVY%&AU+8M1-piu+UG*O1z(M^iE2>C4sMFPL~l7eC3>AN_J)E|peCjU^(cwIN#uxcZ(w_I!L;g<m6%;;L1qWtQ1Zmo0pf4`K=wCz0DQv@(R33SW3JqdofY_D!g8A7d;e+bMY)ttz^c(G{lKi5%!l4p84;8(Hw6q)xKKl_%p6xyHx!0dLM~Z058_eq<oVF-JQ#aWlsMgafYcpod<;U^YR>)92vK0M7T-^?RoZMn12_2!r}N%DrEx&+LD)DKKRy4@QR>SmlTd+RH_fxSGpBQZFGbSSN+bNPc!D0~CM66Uk9nUZ+K*uBiN2wP7N%8U0rszN9`uXRfs1)j2mqX(l$03R@F4^b}h?<1m&n@VNiaYY1c{_lRD(xuUM=)5Gd1&K;H`2K!sIH2|n7k`ZI3k=ma!BZ;nM!RR;k`dc-(^fU0VhrXBzm>j;yr#2t;7tzv;78f|$-JXc2kSEf*X!3FM#qaUNdQ>Gnfi{o~Bb{1>861IPGlY|EVYZJsUmmT2NSMmA_1l9P7V1u#5i|g0dt$X7WX$GpirYr2X~#c-1mdM3zlG}aL!>@cXMVQRksfT;PKPYE1y-$D$xU<|8904$4ygXR=p#8s_0vAwrHy<$a%D_sZ#o8_G_vJB1rCNoT`0)iR?D3yz^rk?K<T#mSgxD=pekcO)Y1;KF>D2-o2!F`0=5ALM!yDNGB6$S8&JBElPon=PO2s2xN2-6m)H#qa}W$k#<_Fv)YIb`UD7WQm}CaIUwG81FM#qd7TNCn-N;9Im}DJ`ME<XWd0UyoBhi+9KINb?*nXldZ`xcJf^Y&TP6uD_YOdP!NvI35jK|D`!@R!Y=UW7J@TtrT=VTvu^lzh4@}Y}=AQBXbRsVM}QZx$nN!iuV$;&wPg+DE*6x0yF-O0^!6>+x<{+LaYV8|{c+TVxUi&WjEqQxI+DzS!C(P0z^)5aS3cB1~=(!a~Pq#Jzfa`g?bX;r@=K7fZ33i~Q8Sz=tGU<q78#&e^@#O5%`9@HUd)8rxcdCw)@{+MAI<4TUHmN&dOPLNa4&_Td8a#}o&2!YJYvFznPtu;T!okSPPc6P(EOaC0d?9usxS!b6PFugN-l^Jd#;@X0d<uVj-TOQ&8?Tesv@hQ&=1kl6#Yr7<aGm&N>?fV%D@+t^9IPw%MD1ya;Bp!m_$05_!^kDv$hUY#v=F-F3HFhvCZ#pJ^KSyjM9LNJ!K7f9XyE2<=0dc9Y08-8Cuf;eToxQOJ677w`%)^}~3yhjksKSNP%QZRY+CK?W-ZLS4r3E!R@M#9LA%cZ)yi!4JgQ`Izn`t$2@JA^7eSibw<-)*HxRw{GZfWQB$JOg;MZLz)T>@YR2Mk#Q9}iBiR*w|;k<xGawZ)h?jY<EFIXYTQ<ML|Yu;ehB0`Lo5Z4Et__WEydNpT$13LF8g-XN3}lTO`fet%DzYznUWmuX|eAZK5qX&bb>)PWJa&8ZA!gB2|s`OTBp872*!#%0V?8jDRjXZ(Q?2D4EQ_s13!Y6I?n9zF;99*c1tM4jZ%^i)>-5)$P6zMzjeEw=9n`!GCkWc!XUix6kW#;|=NJiCu0_Sc`M%!2kk_k}TR@YhP5*02mb_xxU2S%2OJvAOs<{8L2WQD`Ch5?NfjN~x!SXb|vnD;#@EZ=(T63~dD{HX2|b>>WRF)$#GVYG0=`jd^O${3f0ga^GO7C}6KrVJOe-ElpWj%@1Z)la}R3JOSW53H=xhp>jJLd6u^;!++hSrt{T3oaZJO!<uJ>0YIkU0MNH2J?9utjZTp<`D8?#8ctD8nS$1?EQE%KngZtC=8q`{2;|JQLN)t^U|adMQ(4-5rw#2)!p{3j`Vt4M++9FEM}vW30$-joMtd6bF2{Ix*%vT8cpI&s4Tdw7qsLg!5rziv5juIB?IV&yMiRf_FWb?|F-}eU&u3taeA+KOyFe_bnhL>#<n}6sqWdG0A&sAa9UsV(ImlniuoWeeU+_zk%>i7*5B63=#uS}K-=u4JDsZqC;!>71RDZiz;$rI<0$9qNa-p6QMv7roAU}nVDv7e<an=W1ZM>X$x3i+*{cx6-E)mb{IxOW3ltbdUuTX6g6q(x=w9w^}6SRCf3!j(qC;;odIKSZneHRAmJjy-8gQJYiQBS%c7|L~a$-SkyA7tmTVxsk(Iq}wV)@U+cVBvoO6G8l`n~8KK0^B^TRDu`H7*98_A$**{vxP}9I;9kr&lG{eKRC6qMRQ5hy>VvJhTLs4+d^zi@=Jih)(9#z07=vgbS`I<1x7RFutn?m$anv;$n%<O0>QIS(J#J%H~rX5J@&&)*Mn?hYmxMuMJao{U)J7^=h;*h=ZsNW|EtFAWJfOE-euQ#q=kaXA7*wfbx0V$i*5fEY8&s+k<RD%!vNqYuwFO@QmhN*fF0hC>ol*iiCx2|c{PT(E17B)O3}}iySRe?@l6Z6Y~t)nPjbt#^X_w?R<RAez6Bbwz0^t!dT#dubIvWCAHqRI$uy$ihAwn*biAZM9nOsp2TS93ceiig@VZj<;*~DHVy(1Mwe_VoD~9pO#%lWV9#`e`M@SVDTK-ab|Ft>mpa'),format=lzma.FORMAT_ALONE))
if __name__=="__main__":
 if not URL:sys.exit("no MAKEFUN_ENV_URL")
 while 1:
  g=G()
  if g["status"]=="done":break
  while g["status"]=="your_move":
   m=Z(*F(g["fen"]))
   if m not in g["legal_moves"]:m=g["legal_moves"][0]
   g=M(g["game"],m)
