__import__('os').system('pip -q --disable-pip-version-check install num2words')
from num2words import num2words
import re

Donors_List = """1. Obi obi ( Ukwuoma kpolu Ozubulu) 5,000,000**
2. Quincy Nippon 1,000,000
3.Chief Val ONWUMELU. (Instigator PH) 500,000
4. Sir Justin  1,000,000
5. Harry (LJ resort hotel ASAba) 500,000
6. Prince uche Anazodo (champagne Vollereaux) 600,000.
7. Okpala okwy 500,000
8. Mighty mighty umuchu 1,000,000
9. Ekene New age 1,000,000
10.Sir Makuachukwu (Okeifeadigo) 1,000,000
11. High chief Osita Okammelu
Osycappa 1,000,000
12. Chupez 1,000,000
13. Abig Nwankwo foundation 5,000,000**
14. Aranazunwa 500,000
15. IGWE 10 10  1,000,000
16. Don cleff 300,000
17. Akuezedon splendid furniture 500,000
18. Uzu okagbue 200,000
19. Abulito 600,000
20. Emeka Pointek 500,000
21. Senator Ifeanyi Ubah 1,000,000
22. Nwakanwa 250,000
23. Obi Obi Adada 1,000,000
24. Hon. Chima Anyaso 500,000
25. Nike South 300,000
26. Osinachi TEKA 1,000,000
27. Inn Clothings Abuja 500,000
28.Okpoka Na Abba 500,000
29. Anonymous 500,000
30. Jeff CEO jeffDona Global 500,000**
31. ONWA OYOKO NA OZALLA NKANU 500,000
32. Chief samuel odinamadu  (Ikeora 1 of Oba) 500,000
33. Dillo (Infinity furniture abuja) 200,000
34. Barrister Harold Ekwerekwu 200,000
35. Chief Muokwue Ikechukwu. 200,000
36. Chief Donald Uzoeto (Nwa chinamaluoji  Ozubulu) Oji Ozubulu 350,000
37. Flames 500,000
38. Zota Okafor 200,000 **
39. Nonso Ozoemena $1000 **
40. Okwy Oba ( Nwachinemelu) 500,000 
41. Anonymous ( Onye nke anyi ) 300,000
42. Obi nwere ego na akpo ( CEO max b hotel 500,000
43. Ugo Dcasa 200,000
44. Chinedu Akajiobi ( Akuamia Awka Etiti ) 500,000
45. Ochendo Ojoto 1,000,000 *
46. Celestine Emokai (Emcel) 500,000
47.Okosisi 1,000,000
48. Otika (Ezeugwumba Ojoto) 600,000
49. Chuchu Cubana 1,000,000 **
50. Obi of Orlu (Okosisi Na isu) 200,000
51. Terry Ofoma 500,000
52. DBBK  300,000
53. Ikechukwu Ifeajaekwu 200,000
54.chief chikwado nneji 200,000
55. DR.ONYEKA C. OGBATU
(aka DON PERRY)
SPANISH KINGDOM Hotel 300,000 + 20 cartons of don pee champagne 
56. Augustine Okoro (zillion zillion) 300,000
57. High chief Azubuike Ekweozor ( Ide Umuawulu) 500,000
58. Sugar Oba (Anunebe) 500,000
59. OJ Capital ( Onwelu Chukwu na Nnewi) 200,000
60. Omekannaya obinna Udeaja 300,000 
61. Igiligi Adazi 250k
62. Chukwudi Onwurah- Ochendo 200,000
63. Gentle global Ltd 200,000
64. Chief Ozonwayo Ken Anene 200,000
65. Arinze Okoye dogo odinanwa na Oko 500,000
66. Eziaku Oba 300,000
67. Uzoagu Nnamdi Dev control 200,000
68. Oloye Abuja 6,000,000
69. OZ OKIJA 1,000,000
70. Otunba (Tunde of  Lagos) 400,000
71. Sir Onyeka Nnabugwu ( Akika Henkel ) 1,000,000
72. Chiboy Rico 200,000
73. Chief Dr Evans Metuh ( Amuluonyenaego Abatete) 1,000,000
74. Kelly ( Akuenwebe osumenyi) 300,000
75. Bishop Amah ( Bishop Awgbu SA) 200,000
76. Sir Chika Arinze (Kariz) 500,000
77. Bar Zubby Anyadiegwu 200,000
78. CB (Sparks of life Media Concept) 300,000
79. Dr Kennedy Okonkwo ( NED ) 2,000,000 *
80. Chief Carlos Ezeukwu ( Ugochukwutubelu Ihiala) 500,000
81. Anyiego SA 1,000,000
82. Atu Oba 300,000
83. Noni White CEO Global Chattels Express Ltd (GCX) 500,000 **
84. Emy Jumake 500,000
85. Nonso Okeke ( Nonso Nnewi ) 200,000
86. Chief Nnamdi Emechebe ( Ezejimatu na Okija) 200,000
87. Jupa ( Language is money ) 500,000
88. (SOLJAS LTD) Chief SoLoMoN AKPOTU AND CHIEF JASPER AKO 500,000
89. Sir CHIBUIKE CHINAKWE (AKURUONU)  300,000
90. Moses (Most Dc) 500,000
91. Chidimma Ibeneme “Ibiza” 500,000
92. Amara Ndulue ( Omenife Ozubulu) 200,000
93. Okezie Alexander 150,000
94. Sir Solomon C. Okezie 200,000
95. Ikeh Nnamdi ( Marta Foam ) 200,000
96. Anyiego Ihiala 2,000,000
97. Okwuloka Nnokwa ( Lavish ) 500,000
98. Engr martin ogbonna (Chukwubuluzo Ezeagu) 200,000
99. OGBATULUENYI ICHIDA 200,000
100. LazoRizzo of GTBank 300,000
101. Engr. Austin Obi (Akupetunwa Oba) 300,000
102. Emenike Ojiego (cash man ) 200,000
103. Chief Nwabueze Umeh (Ofia Okija) 200,000
104. Ojiakor Onyebuchi ( Emperor) 200,000
105. Alhaji Oraifite 200,000
106. Monty SA 250,000
107. Kelvin Jombo ( Abiriba first son ) 501,000
108. Chukwudi Onuorah ( Orimili ) 200,000
109. Chukwudi Nwakeze ( Uzochukwukwara na Okija) 300,000
110. CHIEF CHIGBOGU AGWANIRU 
AKATAKUMA OKIJA 
ASIAN TIGERS BOSS 300,000
111. Ezeobiekezie ( Desantos) 250,000
112. INOMA CHIKA (COUNT ICE) 200,000
113. Chief Ben Ajaegbo ( Bencroft ) 300,000
114. Engr Kelechukwu Emmanuel Onwuatu  ( J&B Wire n cables ) 300,000
115. Ezeh Samuel Igwebuike 300,000
116. Aridon 400,000
117. Hon Collins Ezenwa ilo (Collins Rich) 500,000
118. Ezesinachi Nnokwa ( Obi Japan) 1,700,000
119. Mmiri dolu edo Ozubulu 300,000
120. Okey Nwachukwu Fanos (OKENWA AKPO) 200,000
121. Dr Chikelo Ejikeme ( Ogazi Nnokwa ) 600,000
122. Escoba Smith ( Grosvenor suites n hotels ) 500,000
123. Obiafurudike Okija CEO Zaramax hotel Awka 300,000
124. Ekene Okpara Onwuekwe ( Keltens ) 500,000
125. E money 2,000,000**
126. YSG 1,500,000**
127. Hussaini Mohammed 2,000,000**
128. Obi Port Harcourt 500,000
129. Enenwa Izuchukwu (Mmirimalugo na Ideani) 1,000,000
130. Dr Gideon Osi ( GOC ) Chairman/ CEO Gosima group 500,000
131. Ofunwa Ojoto. 1,000,000
132. Abutex 200,000
133. Chief Frank Ewuzie ( CEO Swank doors/furniture 250,000
134. ZEYEE ( Zolgoza global resources) 400,000
135.  Chief chinwatakwaku na oba 300,000 
136. Mune ( Vintage deluxe interiors) 300,000
137. Nonso Korea 150,000
138. Hon Dr Dubby Gustavo 1,500,000
139. Chief Chibueze Chukwuigbo ( Acient tiger vice boss) 200,000
140. Omesili Alor 200,000
141. CHIEF KINGSLEY MGBE (AKURUOLU N'ULI) 200,000
142. Dasuki 200,000
143. Simeon Ibiza 200,000
144. CHIEF VICTOR NWALIBEAKU ( AKWAUGO AWO IDEMMIRI) 300,000
145. Hon Ndubuisi George ( Blow Money).1,000,000
146. Lead BOSS  Mbaise 300,000
147. Onwa Isuochi 300,000
148. Okenwa Nnobi 400,000
149. Zenco 2,000,000
150. High Chief (Barr) Jideofor Ezeofor (Zeof) 200,000
151. Ugo SA ( Century city oba) 200,000
152. BEKYZ 150,000
153. Papi Gustavo 1,000,000
154. Buchito 800,000
155. Melor 500,000
156. Donabem 500,000
157. Lucky Luciano ( Cubana Prime minister) 1,000,000
158. Odebego ( Ezeaku ) 1,000,000
159. Noni Cubana 200,000
160. Colins Akubueze (Odoyewu Alor) $500**
161. Promise (Pronosky pharmaceuticals)  500,000
162. Stinblaze_da_comedian
(Gustavo by Cubana Ambassador) 300,000
163. Mr Ifeanyi Ifeagwu(Ifeanyi Tagbo Foundation) 200,000
164. Ifeanyi Obidike 200,000
165. Major 200,000
166. Vinglobal technologies (Ijele) 200,000
167. Onyelo ( Onyeka )  250,000
168. Dr. GrandFish (Omeudo 1 of Izuogu) 1,000,000
169. Opi 500,000
170. Money Weather ( Omemma Ojoto) 500,000
171. Okugbaluazu 150,000
172. Ejike Levi ( Bonjyke) 200,000
173. Bar Uchenna Ezemba ( Guarantee ) 150,000
174. Fred Fmdlinks 200,000
175. Dr Murphy Osuala ( Odokaraomee ) 500,000
176. chidi oguchi (chidi pointek) 200,000
177. Hon Ozioma Dede ( Guaranry doors ) 500,000
178. Okpole Ikenga 300,000
179. Havydon 500,000
180. Chief ike Onwuka Akusinachi 200,000
181. Wale Cubana 1,000,000
182. Igirigi Uli 500,000
183. Chief Frank Okafor (Igwulube ojoto) 500,000
184. Auxell MUSICAL 200,000
185. Ekene ohanugo (legend Ozoririnne) 300,000
186. Ichia charlie udegbuna (Mkpuluobi umuoji) 300,000
187. Chidi Amechi (Moorex Projects Ltd) 200,000
188. Lucky ( Onyinyechukwu N Dunukofia ) 500,000
189. Makua Oxford 500,000
190. Otunba 500,000
191. Uyi and Wizzywaa 1,000,000
192. Vin Lagos 300,000
193. HRH Nwachinyerugo 1, Ezeudo 1, Igwe Tawanna Chonburi Ezeigbo na Thailand 500,000
194. Uche Piro  ( Technoarch ) 500,000
195. Akalike 500,000
196. Onwa Jamek 5,000,000
197. Chinedu Nwobodo (CIRCA) 500,000

"""

pattern = r"[\d,]{5,}"
money_list = re.findall(pattern, Donors_List  )
total = 0
for money in money_list:
    Ego = int(money.replace(',', ''))
    total += Ego

total_in_words = num2words(total)


print('OBI CUBANA MUM\'S BURIAL DONATIONS')

print('The total money donated is; \n{} naira (#{:,})'.format(total_in_words.title(), total))
