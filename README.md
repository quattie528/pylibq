# ktest
Trial to open part of my module works

- 作成日 : 2019年5月19日
- 
- 自分の中ではかなり人生的決断ですが、自分のPythonプログラムを一部公開することにしました。
- テクニカルには、githubが使いこなせていないので、アップロード方法がいけてないかもしれません。
- 
- https://github.com/quattie528/ktest/
- 
- 目的は2つあります。
- 
- [1] 公開をしたほうが情報が集まり(第三者からのフィードバック)、結果的に自分のプログラムへの理解が深まるという予想に賭けることにした
- [2] 実践を通して知財に関する理解を深まるだろうという見通し
- 
- 以下は、この決意をした背景を記述するものです。一般に優しい文章ではないので、ご関心のある方のみを対象としています。
- 結論部は最初に述べたので、後は寛容な読者に身を委ねることによって、公示効果を託そうと考えています。公示効果はFacebookとGithubの冗長構成(片方が駄目になっても別の片方で存在を保つしくみ)でシステム上担保され、不特定多数の読者の意識が保障します。
- 
- 第三者からはぶっ飛んでいると思われるのも自覚していますが、こういう性格で長年やっていて、周囲の反応も多少は予想できるようになったので、他人の視線を気にしていては独立した人間にはなれません。
- ただ、わかる人は全文の行間から、世界の信頼に賭けている点が読み取れるはずなので、批判的文章もあるものの、基本的には前向きな文章に読めるはずです。少なくともFacebookの検閲に摘発されるような内容ではないはずです。
- 
- 
- (注)
- 今まで第三者への提示をまったく想定して作っていなかったので、ちょこちょこ修正アップロードをするかもしれません。余計なライセンスによる著作権表示は削除しました。冒頭のGNUライセンス表示で十分だし、本当はこういう権利主張がしたいわけではなく、単純に悪意ある第三者への牽制は確保したいことだけが問題ですが、悪意ある第三者のためにトモダチを見捨てるのは情けない図です。
-
*************************************************
- 
- [目次]
- (1) きっかけ
- (2) 公開対象
- (3) 独占欲の問題
- (4) 知財に関する覚書メモ
- (5) 最後に
- 
*************************************************
- 
- (1) きっかけ
- 
- 公開をしようと思ったきっかけは今週職場である同僚と会話をして、今までの自分の中のぼんやりと課題と感じていたものがつながって早期の対応しなければならないという直感が働いたからです。
- 今までの自分はプログラムを人に渡すとことに強い拒否反応がありました。ただ、薄々と拒否反応の限界にも気がついており、共有のテクニックをどこかで身につけないといけないと考えるようになりました。
- 
- 直接のきっかけは同僚に渡すことです。なぜ渡す気になったかというと、Pythonで今まで自分ができなかったこと(調べるのがとてもめんどくさいこと)をいとも簡単に譲渡してくれて、その労苦をタダで受け取ることは著しく正義に反するという直感が呼び覚まされたからです。エンジニアという人たちは「ググレカス(ggrks、自分でGoogleで調べろの意味)」と言って調べないことを非難する傾向があるという偏見がありました。おそらく自分が長年の修練によって身につけたノウハウを簡単に渡したくないという独占欲や、技術以外のところでは自尊心が満たされていないという悲哀が予想され、自分にもそういう気持ちはあるので(笑)同情できるものの、たいていの組織体を前提する場合には不毛なパワーゲームで対立するだけです。
- しかし、この悲しさを打ち消す、気軽な「あげるよ」は恩着せがましさもなく、自然な印象を与え、まさに自分がほしかったノウハウだったという主観と客観が美しく結晶した瞬間として心の中の革命と呼び起こし、これは真剣に考えなくてはならないと思うに至りました。両方とも必要だと思いますが。
- 
- 不幸を乗り越えるためにはフロイト風の過去の直視というトラウマ理論が有名ですが、自分はあまりこれを信用していなくて、マイナス感情の反射効果(数式風に言えばマイナス1をかけるだけ)のほうが前向きではないかと思っています。プラス思考の前向きさは単純にプラス加算の蓄積で努力するしかないですが、マイナス思考の前向きさは一発逆転を狙います。
- 
- これは直接の動因ですが、他の諸々の背景として、[A]個人だけで努力することが限界にぶち当たっていること、[B]職場でソフトウェアライセンスの取扱にあたって本格的に知財への一定の理解をしようと決意したこと、[C]時事的にマイクロソフトの最近の変貌(特にSatya Nadella CEO)に触発されていること、[D]昔に比べると一定の支持者が存在するという確信が持てるようになってきたこと、[E]今年は大学院時代の幸福を乗り越えようという機運が自分の中で高まっていることなどがあります。ただ、この動因が決定的要素として突き動かされて、提示は週明けと約束をしてしまったので、早急にライセンスポリシーをまとめることにしました。
- [B]については第二の目的にも関わるので、後述します。
- 
- *************************************************
- 
- (2) 公開対象
- 
- 公開対象はモジュールのみで、アプリ部分はひとまず(prima facie)非公開とします。
- 今まで自分のためのみで作ったものなので他の人に役立つかは不明ですが、流行のPyrhonを使ってみたいけど、一人で習得までに時間を要するという初心者から、他のコードの書き方を参考にしたい中級者向けには役立つと思っています。
- 
- モジュールとはプログラムの部品のようなもので、これだけで目的の情報処理は完結しません。アプリとは特定の情報処理を終局的に行うプログラムといったん(prima facie)に定義します。これこそがプログラムの完成形で、すべてのプログラムはそのために作られます。モジュールを通して、自分のアプリの意図が推測できるかもしれませんが、最終形にするまでのデバッグの手間などもあるので、本当のアプリを完全表象させるには時間的距離があります。
- 
- 少しセコい留保が残っているものの、単体では意味をなさない点が、多少は安心して公開できるポイントです。ただ、部品はプログラムを動かすにあたって重要な要素であり、pandasという別格の部品(しかも無償!)も世の中にあるので、部品だけかよという批判は的外れです。情報処理の連環の中で、途中のプロセスに重要部品を選ぶのはプログラム全体を構成するにあたって重要な選択です。また、部品のほうが抽象度が高いので、使い回しもされやすいので、本当は一般ウケするはずです。なお、公開モジュールで最もよく使うのは「xt.py」「xx.py」「datsun.py」の3つです。
- アプリは具体的処理を対象とするので、個人の意図が明確に表れやすく、その内心はまだ隠したい心情が残されています。このセコい留保は許容していただきたいという消極的狙いとともに、途中段階のものだからこそ個々のアプリ完成までの質疑応答が触発される積極的狙いもあると思っています。個々人の情報処理の目的は異なるはずで、中間処理の共有こそが柔軟性のあるノウハウの共有につながると考えています。
- 
- ただ、会社関連で使うアプリに関しては公開してしようか傾いています。一番の障害は、職務発明や職務著作の関係の理解が完全ではないため、モジュール公開による過渡期状況を見てから考えます。「法人(略)の発意に基づき」(著作権法15条2項)という記載から、個人帰属の可能性が有力ですが、確信にまで至っていません。もしも、(1)知財に詳しい方、または、(2)人文的感性に理解のある方との議論が深められれば、この点についても納得感を得た上で公開性を緩めようと思います。個別アプリも性質に応じて、公開性を緩めることを考えます。
- 
- なお、これらのモジュールの多くはエセドイツ語が含まれています。ある時期にコンピュータの公用語をドイツ語にしようと決めたからです。PEP8(英語で書くべしというルール、https://www.python.org/dev/peps/pep-0008/ )に反しますが、可読性が下がるので、万が一のコード漏洩の場合にも知財の観点から理解されない(自分の世界に閉じこもっている)メリットがあります。ドイツ語圏の人たちは読めるかもしれませんが、文脈がわからなければ、プログラムの精神は理解されないだろうという狙いもあります。これらを英語化すべきかどうかは需要と反応を見て考えることにします。
- 
- 日本語化は、日本語を扱う場合のみ考えています。これを国家への忠誠心の欠落と批判することはできますが、グローバル世界の波を考えると日本国に閉じた文脈を確保できるのはメリットです。すなわち、世界に俺のことがわかってたまるか、という気持ちです。なお、日本語がわかっても日本人全員にわかってもらえるわけではないので、言語の通用性はコミュニケーションの条件の一つにすぎません。逆に言えば、母語が共通でなくても、言語以外の要素で補強できることは多少の経験的全体の中に含まれているので、世界に完全に閉じているわけではありません。自己と世界への開閉のコントロールが維持できるかが核心です。
- 
- なお、令和対応は完了しました(「xt.py」164-187行参照)。国家法人説を信奉しているくせに、元号制の意義については理解できていないという致命的欠陥が自分にはあるものの、時代の画期という国民意識を調達する客観的効果に縮減して考えて無害化するべきだと考えています。
- 
-------------------------------------------------
- 
- (3) 独占欲の問題
- 
- プログラムの共有にあたっては相反する感情があります。第一にプログラムを独占したいという感情、第二にプログラムを感動を共有したいという感情です。自分は心の底ではトモダチには共有したいと思っています。タダであげることに躊躇はありまえん。これに付随する重要事項として、嫌いな第三者(本文では敵という少し強烈な言葉を使います)には見せたくない気持ちがありました。
- 
- 世の中は愛に包まれていると同時に憎しみにも包まれています(Love and Hate)。この矛盾した世界観は大前提です(理論的にはThomas Hobbesの強い影響を受けています)。ただ、愛と憎しみの両方が存在するところがミソで、片方に偏る世界観はすべて短絡だと思っています。憎しみの世界に着目すると、裏の世界の暴露の快楽に溺れてしまいます。
- 
- さて、プログラムができると情報処理能力は確実に上がるので、敵の脅威が発生した場合にも、有力な内心の自由(憲法19条)の対抗力を事実上の効力を付帯しながら確保できるので、野蛮な世界においては心強い力を与えてくれます。公開をしたら、敵にも自分の手がバレるという懸念がありました。
- 
- ただ、プログラムに関する情報は公開されていて、昔に比べたらハードルはかなり低くなりました。だからといって誰でもすぐ使えるわけではなく、一定の習得が必要になります。この習得が一つの大きな心の参入障壁になるのは間違いなく、プログラムができる人はこの壁を乗り越えているはずです。この心の参入障壁を敵が超えられるはずがないという確信が独占欲の担保です。大きな壁は最初のセットアップで、この部分が一番つまらなくて、しかも慣れている人でもつまずくので、初心者がここで諦めるのは無理もありません。ただ、この壁を越えると恐ろしいほどの情報処理が可能になり、意図したことが実現できると天才になった気持ちになります。これは本文では重要概念なので、天才幻想と呼びます。天才幻想は敵への対抗にとって覚醒剤並みの効果を与えてくれます。天才幻想に自覚的であっても、心の参入障壁への意識(あのセットアップの俺の苦労)もあるので、これによって人々が遠ざかるという予想ももちろん持っています。ただし、本当は障壁を超えた後にも、デバッグやプロセスの洗練化の課題もあり、これは独占欲を弱める共有への意思につながる事実上の効力があります。ただ、ここを乗り越えてしまう情報処理は更に洗練化されていき、指数関数レベルで情報処理能力が高まるかのような天才幻想がさらに肥大化していくことになります。
- 
- しかし、これが幻想であることは、公開情報という文脈を見れば明らかです。そもそもPythonを作ったのは自分ではありません(作者であるGuido van Rossumへのクレジットを忘れた独占欲が無価値であることを忘れたことはありません)。出来上がったモジュールの力も借りているので、他の人の力も借りています。それでも、どうして天才幻想が肥大化するのかというと、おそらく不幸にして自分はプログラムを独学で身に付けて、ほとんど読書のみで身に付けたのと、亜流であることから組織体からは拒絶されがちという経験的全体と就職市場の言説のシンクロというネガティブな背景が増幅したという自分史の事情がありそうです。敵への警戒心が、拍車をかけます。過去の経験的全体から帰納して独占欲と天才幻想を維持してきた点はやむをえないと思うのですが、一回の「あげるよ」から未来の経験的主体への拡張を見直すようになり、帰納法の最大の弱点であるたった1つの例外(counterexample)の提示による粉砕(Karl Popper)という改革を狙おうという気持ちになりました。これが成功すれば、流行語である「成長」にもつながるはずです。
- 
- なお、自分は天才概念をロマン派の情熱の賜物だととらえていて、たまたまモーツアルトのような古典とロマンの間で生きる人の後に情熱によって市民の力を見せつけたベートーベン[1770-1827]がその音楽によって人々を喚起して焼き付けた画像だと思っています。強固な身分制度への反発に対して、天才という強烈な概念で対抗せざるをえない(敵は神聖ローマ帝国のなれの果てのオーストリア!)、そして確かにベートーベンの音楽は心を揺さぶられるものがあり、人々の模範というカントの哲学(Immanuel Kant [1790] "Kritik der Urteilskraft" = 篠田英雄・訳『判断力批判(上)』岩波書店、252頁)が、古典としての結晶化すると同時に、天才の画像も固定化した一種の喜劇というのが自分の憶測です。なので、もともと天才概念を文脈化して脱神話化して使っているので、天才幻想とわざわざ呼ばなくても、天才はもともと幻想なのです。
- 
- なお、天才の幻想から覚めたとしても、情報処理の事実は見れば明らかなので、この千万馬力をどうするかという問題はあります。社会から悪魔化されると、対抗感情としての天才幻想が再来するので危険ですが、このモチーフが最も美しい形で表現されているのは『アナと雪の女王(Frozen)』(https://www.amazon.co.jp/gp/video/detail/B00KRA2AYC/ )で、才能と愛の組合せによって公益は実現するという普遍的メッセージが読み取れます。しかも、愛が三重(多重)に表現されている点に挑戦したのは見事だと思います。
- 両者をつなげるのは信頼であり、自分は信頼に賭けてみることにしました。
- 
- 本節の自己省察により、プログラムの独占欲は緩和されるべきという結論は、導かれました(週末中に無茶苦茶に考えました)。
- 
-------------------------------------------------
- 
- (4) 知財に関する覚書メモ
- 
- 一方、これは純粋に勤務先の強い要請という背景もあり、今まではぼんやりと職務執行をしてきましたが、一念発起して著作権や特許権の中でもソフトウェアライセンスに限定するかたちであれば、体系的理解に至れるかもしれないと考えて、近くの図書館でいくつか本を借りることにしました。特許権はそれなりに明確で把握しやすいのですが、著作権は複数の支分権が錯綜して、かつ無登記で当然に発生する(無方式主義)というとらえどころのなさが、心から離れる理由です。上皇の時代であることを思い起こせば、職の体系に群がる魑魅魍魎をイメージしてしまいます。しかし、この支分権の実定化は制度設計上のものにすぎず、「特許権の場合は実施の形態ごとに(生産権、使用権、譲渡権、輸入権、輸出権)などと構成せず、これらを取りまとめて実施権と呼んでいる(高林龍[2016]『著作権法:第3版』有斐閣、10頁)」という説明により、一元化作用を目指すことは可能である点に勇気づけられました。
- 同著者によれば、著作権は表現(外見)を保護対象として、特許権はアイディア(中身)を保護対象として、ソフトウェアに焦点を当てれば、外見はプログラムの組み方によって無数に個性的であり得るのに対して、中身は設計施工設計思想というプログラムの裏側にある考えと、内外が分節できるので、非常に明確化しやすいです。ただ、両者の分節は、沿革として旧文部省(文化庁)の著作権と通商産業省の特許権の省益争いっぽい過程があったようですが、実はこれが代理戦争の表れで長い保護期間に着目したアメリカの意向が反映されて前者がいったんは勝ったらしいですが(前著65頁)、21世紀には特許の独占権の強さが着目されて質が重視される(高林龍[2017]『特許法:第6版』有斐閣、29頁)というどんでん返しもあったようで、この分節は自然法か歴史のどちらに由来するかという謎は明かされません。ただ、アメリカの外圧に対しては日本人(少なくとも政策当事者という立場から離れている身)としては喜劇としてとらえれば、笑いながら知財が学べそうです。
- 
- 一方、最近は美学に対する強い衝動が働いていて、多様な表現体が多様な形で感性を刺激する混乱をどのように収束すべきかという課題を感じていて、多様性に対しては理性による統覚と心の感動という一元化尺度を働かせれば、一定の安定した理解は導き出せるように思います。著作権の問題事例を読むと、多くのパターンは技術の進展による表現媒体特有の性質をどのようにとらえるかに終始され、これが支分権の錯綜をもたらします。しかし、結局は相手にするのは表現(外見)であるという共通点はあるので、一番の方法は、よく見ることです。
- 
- 知財にとって一番理解がしにくいのは無体という点以外に、その成立ともに不知の人たちに対しても侵害が観念できる点です。著作権法や特許法には損害賠償や侵害というネガティブな言葉が並びますが、不知(善意)を保護するはずの法の精神の大原則を考えると警告や請求で良いではないかと思うものの、不当利得という表現は弱いかつネガティブなニュアンスが含まれるのと、意思主義の観点からは契約の成立が観念できないのが制度設計の難しさなのかもしれません。むしろこの問題を誠実に対応した場合の理想的制度のあり方は非常に知りたいのですが、地味に本を読まないと理解に至らなそうです。アメリカ憲法(1-8-8)のように知財宣言をしておけば、国民自らの包括的宣言により不知は存在しないというフィクションは一つの方法ですが、アメリカでしか通じないし、本当に現実のアメリカ国民が納得しているかは疑問です。
- おそらく知財の弊害は世界でも認識されていて、ソフトウェア無限にコピーができる性質を認識しつつ、作者の労苦は報いたいという気持ちと、コミュニティを助けたいという公共心をどう育むかという難問がある中で、驚異的な回答を出したApacheライセンス2.0の3条の存在を知りました(https://www.apache.org/licenses/LICENSE-2.0 )。簡潔にいうとApacheというアプリは自由に使えて、他の知財との組合せも許容されるが、特許に関する訴訟を提起した場合にはApacheの許諾が消滅するというものです。知財の有効活用を推奨するとともに知財の権利濫用は許さないという構成を条文で表現するのは自由の表れであり、これを私的自治と商業界で実現しようという点が一段と公益への連結という点から優れていて、これを考えた人は天才ではないかと思いました。日本国憲法32条との対決というギリギリ合憲になりそうなテクニカルな点も自分好みです。
- まだ覚書段階の理解しかないですが、こういう情熱が起点になれば、わかりにくい知財も深められるという見通しがあるので、プログラムの公開によって共有感情を身につけていけば、知財の当事者として実践知がつきそうです。
- 
- ※と書いておきながら、ライセンスはGNUにしました(知財の理解の深まりにより変えるかもしれません)
- 
-------------------------------------------------
- 
- (5) 最後に
- 
- 上記のような肯定的心情がバネとなり、冒頭の2つの狙いを心理的に整えられるようになりました。
- 
- [1] 公開をしたほうが情報が集まり(第三者からのフィードバック)、結果的に自分のプログラムへの理解が深まるという予想に賭けることにした
- [2] 実践を通して知財に関する理解を深まるだろうという見通しがある
- 
- いつまで続くかはわからない短い会社人生の中で言えるのは、プチインテリは組織に属したからといって死滅するものではなく、心の持ちようと生まれてしまった自然体が決めるものだという帰納的結論があります。日本国には幸いにしてモデルとなるビジネスマン(北野一氏、山口周氏)がいて、少数かもしれませんが先人の存在を見ると、特に自分のアイデンティティを放棄する必要もないという安心感も得られて、のらりくらりと生活できるようになります。公開後にも、のらりくらりが続くかは、新しい信頼の領域に身を委ねてみて、自己意識の表象が立ち現れないとわかりません。
