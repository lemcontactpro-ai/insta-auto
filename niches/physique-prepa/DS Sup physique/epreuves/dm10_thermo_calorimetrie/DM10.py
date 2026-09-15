import numpy as np # importation de la bibliothèque Numpy
import numpy.random as rd # importation de la bibliothèque random


cL,cS=4.18,2.09  #on définit les capacités thermiques massiques de l'eau
Tfus=0           #on définit la température de fusion de l'eau sous une pression de 1bar

N=10000          #on définit le nombre de tirages aléatoires réalisés


# PARTIE a.

#on introduit la valeur de m1 et la valeur de la demi largeur de l'intervalle de confiance associé
m1,lm1=95,1.05
#idem pour m2, T1 et T2
m2,lm2=69,0.79
T1,lT1=20,0.1
T2,lT2=50,0.1
TF,lTF=31.3,0.1

#Les lignes suivanes permettent de déterminer l'incertitude sur la mesure de m1
#par la méthode de Monté Carlo

# on créée une liste de N tirages aléatoires dans l'intervalle de mesure pour la masse m1
#en supposant une distribution uniforme des tirages
m1_MC=m1+rd.uniform(-lm1,lm1,N)

#on vérifie que l'évaluation de m1 par la moyenne de la variable aléatoire est correcte
moym1=np.average(m1_MC)

#on exploite l'écart type pour évaluer l'incertitude u(m1)
um1=np.std(m1_MC,ddof=1)

print('L évaluation de m1 est :',moym1,'g \n et celle sur l incertitude est u(m1)=',um1,'g')

#Ecrire les lignes correspondantes pour m2, T1 et T2
m2_MC=m2+rd.uniform(-lm2,lm2,N)
moym2=np.average(m2_MC)
um2=np.std(m2_MC,ddof=1)
print('L évaluation de m2 est :',moym2,'g \n et celle sur l incertitude est u(m2)',um2,'g')

T1_MC=T1+rd.uniform(-lT1,lT1,N)
moyT1=np.average(T1_MC)
uT1=np.std(T1_MC,ddof=1)
print('L évaluation de T1 est :',moyT1,'°C \n et celle sur l incertitude est u(T1)',uT1,'°C')

T2_MC=T2+rd.uniform(-lT2,lT2,N)
moyT2=np.average(T2_MC)
uT2=np.std(T2_MC,ddof=1)
print('L évaluation de T2 est :',moyT2,'°C \n et celle sur l incertitude est u(T2)',uT2,'°C')

TF_MC=TF+rd.uniform(-lTF,lTF,N)
moyTF=np.average(TF_MC)
uTF=np.std(TF_MC,ddof=1)
print('L évaluation de TF est :',moyTF,'°C \n et celle sur l incertitude est u(TF)',uTF,'°C')


#On construit alors les N évaluations de Ccalo issues des N tirages aléatoires précédents
Ccalo_MC=cL*(m2_MC*(T2_MC-TF_MC)/(TF_MC-T1_MC)-m1_MC)

#On évalue la capacité thermique par la moyenne sur les tirages
Ccalo=np.average(Ccalo_MC)

#on évalue l'incertitude associée
uCcalo=np.std(Ccalo_MC,ddof=1)
#on affiche
print('\033[0;33m L évaluation de Ccalo est :',Ccalo,'J.K^-1 \n et celle sur l incertitude est u(Ccalo)',uCcalo,'J.K^-1 \033[0m')

#ce qui donne pour la masse équivalente en eau du calorimètre.
µ,uµ=Ccalo/cL,uCcalo/cL
print('\033[0;33m la masse équivalente en eau du calorimètre est µ',µ,'g \ et l incertitude associée est', uµ, 'g.\033[0m')



# PARTIE b.

#pour l'évaluation de cfe, on mesure
me,lme=??,??
mfe,lmfe=??,??
T3,lT3=??,??
T4,lT4=??,??
TF2,lTF2=??,??

#on fait les évaluation des moyennes et incertitude par MC
me_MC=me+rd.uniform(-lme,lme,N)
moyme=np.average(me_MC)
ume=np.std(me_MC,ddof=1)
print('L évaluation de me est :',moyme,'g \n et celle sur l incertitude est u(me)',ume,'g')
mfe_MC=mfe+rd.uniform(-lmfe,lmfe,N)
moymfe=np.average(mfe_MC)
umfe=np.std(mfe_MC,ddof=1)
print('L évaluation de mfe est :',moymfe,'g \n et celle sur l incertitude est u(mfe)',umfe,'g')
T3_MC=T3+rd.uniform(-lT3,lT3,N)
moyT3=np.average(T3_MC)
uT3=np.std(T3_MC,ddof=1)
print('L évaluation de T3 est :',moyT3,'°C \n et celle sur l incertitude est u(T3)',uT3,'°C')
T4_MC=T4+rd.uniform(-lT4,lT4,N)
moyT4=np.average(T4_MC)
uT4=np.std(T4_MC,ddof=1)
print('L évaluation de T4 est :',moyT4,'°C \n et celle sur l incertitude est u(T4)',uT4,'°C')
TF2_MC=TF2+rd.uniform(-lTF2,lTF2,N)
moyTF2=np.average(TF2_MC)
uTF2=np.std(TF2_MC,ddof=1)
print('L évaluation de TF2 est :',moyTF2,'°C \n et celle sur l incertitude est u(TF2)',uTF2,'°C')

#on évalue la capacité thermique massique du fer

cfe_MC=??
moycfe=??
ucfe=??

print('\033[0;33m la capacité thermique massique du fer est cfe',moycfe,'J.kg^-1.K^-1 \n et l incertitude associée est', ucfe, 'J.kg^-1.K^-1. \033[0m')

# Partie c.

#pour l'évaluation de Dfush, on mesure
ml,lml=??,??
ms,lms=??,??
T5,lT5=??,??
T6,lT6=??,??
TF3,lTF3=??,??


#on fait les évaluation des moyennes et incertitude par MC
ml_MC=ml+rd.uniform(-lml,lml,N)
moyml=np.average(ml_MC)
uml=np.std(ml_MC,ddof=1)
print('L évaluation de ml est :',moyml,'g \n et celle sur l incertitude est u(ml)',uml,'g')
ms_MC=ms+rd.uniform(-lms,lms,N)
moyms=np.average(ms_MC)
ums=np.std(ms_MC,ddof=1)
print('L évaluation de ms est :',moyms,'g \n et celle sur l incertitude est u(ms)',ums,'g')
T5_MC=T5+rd.uniform(-lT5,lT5,N)
moyT5=np.average(T5_MC)
uT5=np.std(T5_MC,ddof=1)
print('L évaluation de T5 est :',moyT5,'°C \n et celle sur l incertitude est u(T5)',uT5,'°C')
T6_MC=T6+rd.uniform(-lT6,lT6,N)
moyT6=np.average(T6_MC)
uT6=np.std(T6_MC,ddof=1)
print('L évaluation de T6 est :',moyT6,'°C \n et celle sur l incertitude est u(T6)',uT6,'°C')
TF3_MC=TF3+rd.uniform(-lTF3,lTF3,N)
moyTF3=np.average(TF3_MC)
uTF3=np.std(TF3_MC,ddof=1)
print('L évaluation de TF3 est :',moyTF3,'°C \n et celle sur l incertitude est u(TF3)',uTF3,'°C')

#on évalue l'enthalpie massique de fusion de l'eau

D_MC=??
moyD=??
uD=??

print('\033[0;33m l enthalpie massique de fusion de l eau est Dfush',moyD,'kJ.kg^-1 \n et l incertitude associée est', uD, 'kJ.kg^-1. \033[0m')


# partie d.

#pour l'évaluation de Ccalo, on mesure
m,lm=??,??
T7,lT7=??,??
TF4,lTF4=??,??
U,lU=??,??
Tau,lTau=??,??

#on fait les évaluation des moyennes et incertitude par MC
m_MC=m+rd.uniform(-lm,lm,N)
moym=np.average(m_MC)
um=np.std(m_MC,ddof=1)
print('L évaluation de m est :',moym,'g \n et celle sur l incertitude est u(m)',um,'g')
T7_MC=T7+rd.uniform(-lT7,lT7,N)
moyT7=np.average(T7_MC)
uT7=np.std(T7_MC,ddof=1)
print('L évaluation de T7 est :',moyT7,'°C \n et celle sur l incertitude est u(T7)',uT7,'°C')
TF4_MC=TF4+rd.uniform(-lTF4,lTF4,N)
moyTF4=np.average(TF4_MC)
uTF4=np.std(TF4_MC,ddof=1)
print('L évaluation de TF4 est :',moyTF4,'°C \n et celle sur l incertitude est u(TF4)',uTF4,'°C')
U_MC=U+rd.uniform(-lU,lU,N)
moyU=np.average(U_MC)
uU=np.std(U_MC,ddof=1)
print('L évaluation de U est :',moyU,'V \n et celle sur l incertitude est u(U)',uU,'V')
Tau_MC=Tau+rd.uniform(-lTau,lTau,N)
moyTau=np.average(Tau_MC)
uTau=np.std(Tau_MC,ddof=1)
print('L évaluation de Tau est :',moyTau,'s \n et celle sur l incertitude est u(Tau)',uTau,'V')

#on évalue la capacité thermique du calorimètre
Ccal_MC=
moyCcal=
uCcal=

print('\033[0;33m la capacité thermique du calorimètre est Ccalo',Ccalo,'J.kg^-1 \n et l incertitude associée est', uCcal, 'J.K^-1. \033[0m')



