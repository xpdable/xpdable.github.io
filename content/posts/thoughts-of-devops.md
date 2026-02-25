---
title: Thoughts of DevOps
date: 2023-07-11
tags: [devops, culture, ci-cd]
---

Almost ten years ago, when I first heard the word **"DevOps"**, I was working as an automation QA engineer. I was quite unhappy that the idea of combining **Development** and **Operations** seemed to leave **testing** behind.

At that time, my team was responsible for automation testing. Since we followed a **waterfall model** with quarterly releases, we had plenty of time to refine and improve automation before the release. But when release day came, it was always a scramble. Development, QA, and release teams were all under pressure. I still remember the chaos clearly — and I bet many of you have experienced the same. Failed test cases were brought to developers at the last minute. They had to decide whether to fix them immediately or postpone to the next release. Hotfixes were patched, and release engineers rebuilt packages — sometimes this process took hours, and it happened daily during the release phase.

![Release day chaos](../assets/releaseday.png)

Things started to get better when we made the decision to **decouple several features** from our monolithic architecture. This allowed developers and release engineers to generate **weekly or even daily builds**, so that QA could begin testing earlier. It helped a lot. We had more time to automate test cases for new features and bug fixes, and by the time the formal release came around, most of the verification had already been automated. This was when the DevOps wheel began to turn in my world. Over time, our daily builds evolved into a proper **CI/CD discipline**, and now, automation builds and deploys code even on each commit.

It sounds like a happy ending — but does this really help? What happens when the DevOps process doesn't actually improve development efficiency?

## DevOps should never be about doing it for the sake of doing it.

Let's step back and look at the bigger picture. As buzzwords like **DevOps** and **DevSecOps** become more mainstream, many companies — especially those going through digital transformations — are quick to adopt them. And while there are countless glowing success stories out there, many of them miss the **core objective**: **accelerate the delivery of value, while maintaining high quality and reliability.**

Instead, we hear things like:

> *"We've built a CI/CD pipeline. We're doing 10 production releases a day. We're fully practicing DevOps!"*

But DevOps should never be about doing it for the sake of doing it.

Several years ago, I was leading to define and measure DevOps KPIs at the enterprise level. Naturally, I started with the **[4 Key Metrics](https://dora.dev/guides/dora-metrics-four-keys/)** (deployment frequency, lead time, change failure rate, and MTTR). But I was caught off guard when management's first question was:

> *"Hey, can we increase our deployment frequency? I have to report 100 deployments per month to my boss."*

![Agile comic](../assets/comic-agile.webp)

That completely missed the point.

I ended up spending a month explaining how to **use metrics fairly and meaningfully**. These metrics are meant to **reflect the performance** of your DevOps practices — not become a target to be gamed. You can improve them by enhancing your CI/CD pipeline, introducing better testing gates, adopting trunk-based development, and more. But doing 100 deployments just to hit a number? That's just noise.

Even worse, I've seen teams being compared against one another purely based on deployment counts.

> *"Why did the gateway application only release once this month, while the API service released 10 times this week?"*

This kind of pressure often leads to meaningless releases — just to avoid being questioned. I've seen teams pushing code with no real changes, just to appear "active". And what's the result? Burnout, wasted effort, and increased risk.

This brings us to a deeper problem: **misusing tools without understanding their cost**. When I joined a new project, I immediately noticed our shared Jenkins instance was always jammed. It turned out dozens of teams were running daily builds on it — including many unnecessary or stuck pipelines. Some of them even had manual approval steps **without any timeout**. This wasn't improving delivery efficiency — it was blocking everyone else.

There are many great technical solutions out there, and DevOps is certainly one of them. But like everything else in tech, **it only works if used properly** — and with the right intention. DevOps is as important as your product architecture, and just as easily misapplied.

There are already tons of tutorials on how to implement CI/CD pipelines. But the **most essential part is the mindset** — how we collaborate, how we improve, and how we deliver value.

**DevOps isn't about chasing metrics or just implementing tools.**
It's about **fostering a culture** of collaboration, continuous learning, and delivering real value to customers with quality and speed. Without the right mindset and purpose, even the best tools and processes become meaningless.

**True DevOps drives teams to work together seamlessly, improve constantly, and focus on what really matters — solving problems and creating impact.**

<!-- lang:zh -->

大约十年前，当我第一次听到**"DevOps"**这个词的时候，我还是一名自动化测试工程师。当时我相当不满——**开发**和**运维**的结合，似乎把**测试**完全抛在了脑后。

那时候，我的团队负责自动化测试。我们采用**瀑布模型**，按季度发布，因此在发布之前有充足的时间来打磨和完善自动化。但一到发布日，一切就乱了套。开发、测试、发布团队全都压力山大。我至今清晰地记得那种混乱——我相信很多人也有同感。失败的测试用例在最后一刻才交到开发手上，他们必须决定是立即修复还是推迟到下个版本。热修复补丁不断打上，发布工程师反复重新构建包——有时候这个过程要持续好几个小时，而且在发布阶段每天都会发生。

![发布日的混乱](../assets/releaseday.png)

情况开始好转是在我们决定从单体架构中**解耦若干功能**之后。这使得开发和发布工程师可以生成**每周甚至每日构建**，从而让测试团队更早介入。这帮助很大。我们有更多时间为新功能和错误修复编写自动化测试用例，到正式发布时，大部分验证工作已经自动化完成。这就是 DevOps 之轮在我的世界里开始转动的时刻。随着时间推移，我们的每日构建演变成了成熟的**CI/CD 规范**，如今，自动化构建和部署已经可以在每次提交时触发。

听起来是一个完美的结局——但这真的有用吗？当 DevOps 流程并没有真正提高开发效率时，会发生什么？

## DevOps 绝不应该为了做而做。

让我们退后一步，看看更大的图景。随着**DevOps**和**DevSecOps**等热词变得越来越主流，许多公司——尤其是那些正在进行数字化转型的公司——迫不及待地采纳它们。虽然有无数光鲜的成功案例，但很多都忽略了**核心目标**：**在保持高质量和高可靠性的同时，加速价值的交付。**

相反，我们经常听到这样的话：

> *"我们已经建好了 CI/CD 流水线。我们每天发布 10 次到生产环境。我们已经完全在实践 DevOps 了！"*

但 DevOps 绝不应该为了做而做。

几年前，我负责在企业层面定义和衡量 DevOps KPI。很自然地，我从**[DORA 四项关键指标](https://dora.dev/guides/dora-metrics-four-keys/)**（部署频率、前置时间、变更失败率和 MTTR）开始。但管理层的第一个问题让我措手不及：

> *"嘿，我们能不能提高部署频率？我需要向老板汇报每月 100 次部署。"*

![敏捷漫画](../assets/comic-agile.webp)

这完全偏离了重点。

我花了整整一个月来解释如何**公平且有意义地使用指标**。这些指标是用来**反映**你的 DevOps 实践**表现**的——而不是变成一个被刷数据的目标。你可以通过优化 CI/CD 流水线、引入更好的测试门禁、采用主干开发等方式来改进这些指标。但仅仅为了凑数字而做 100 次部署？那只是噪音。

更糟糕的是，我见过团队之间纯粹根据部署次数来进行比较。

> *"为什么网关应用这个月只发布了一次，而 API 服务这周就发布了 10 次？"*

这种压力往往导致无意义的发布——只是为了不被质疑。我见过团队在没有任何实质性变更的情况下推送代码，只是为了看起来"活跃"。结果呢？倦怠、浪费精力，以及更高的风险。

这引出了一个更深层的问题：**在不理解成本的情况下滥用工具**。当我加入一个新项目时，我立刻注意到我们共享的 Jenkins 实例总是卡得不行。原来有几十个团队在上面运行每日构建——其中包括许多不必要的或者卡住的流水线。有些甚至设置了**没有超时时间**的人工审批步骤。这并没有提高交付效率——而是在阻碍所有人。

市面上有很多优秀的技术方案，DevOps 无疑是其中之一。但和技术领域的所有东西一样，**只有正确使用才有效**——而且要有正确的意图。DevOps 和你的产品架构一样重要，也一样容易被误用。

关于如何实现 CI/CD 流水线的教程已经数不胜数。但**最关键的部分是思维方式**——我们如何协作，如何改进，如何交付价值。

**DevOps 不是追逐指标或只是实施工具。**
它是**培育一种文化**——协作的文化、持续学习的文化、以质量和速度向客户交付真正价值的文化。没有正确的思维方式和目的，即使最好的工具和流程也毫无意义。

**真正的 DevOps 驱动团队无缝协作、持续改进，并专注于真正重要的事——解决问题、创造影响。**

<!-- lang:de -->

Vor etwa zehn Jahren, als ich zum ersten Mal das Wort **„DevOps"** hörte, arbeitete ich als Automatisierungs-QA-Ingenieur. Ich war ziemlich unzufrieden darüber, dass die Idee, **Entwicklung** und **Betrieb** zu vereinen, das **Testen** scheinbar außen vor ließ.

Damals war mein Team für die Testautomatisierung verantwortlich. Da wir einem **Wasserfallmodell** mit vierteljährlichen Releases folgten, hatten wir ausreichend Zeit, die Automatisierung vor dem Release zu verfeinern und zu verbessern. Aber wenn der Release-Tag kam, war es immer ein Chaos. Entwicklungs-, QA- und Release-Teams standen alle unter Druck. Ich erinnere mich noch lebhaft an dieses Chaos — und ich wette, viele von euch haben dasselbe erlebt. Fehlgeschlagene Testfälle wurden den Entwicklern in letzter Minute vorgelegt. Sie mussten entscheiden, ob sie sie sofort beheben oder auf das nächste Release verschieben sollten. Hotfixes wurden eingespielt und Release-Ingenieure bauten Pakete neu — manchmal dauerte dieser Prozess Stunden, und das passierte in der Release-Phase täglich.

![Release-Tag-Chaos](../assets/releaseday.png)

Es wurde besser, als wir die Entscheidung trafen, **mehrere Features von unserer monolithischen Architektur zu entkoppeln**. Dies ermöglichte es Entwicklern und Release-Ingenieuren, **wöchentliche oder sogar tägliche Builds** zu erstellen, damit QA früher mit dem Testen beginnen konnte. Das half enorm. Wir hatten mehr Zeit, Testfälle für neue Features und Bugfixes zu automatisieren, und bis zum formalen Release waren die meisten Überprüfungen bereits automatisiert. In diesem Moment begann sich das DevOps-Rad in meiner Welt zu drehen. Mit der Zeit entwickelten sich unsere täglichen Builds zu einer ausgereiften **CI/CD-Disziplin**, und heute bauen und deployen automatisierte Prozesse Code sogar bei jedem einzelnen Commit.

Das klingt nach einem Happy End — aber hilft das wirklich? Was passiert, wenn der DevOps-Prozess die Entwicklungseffizienz gar nicht verbessert?

## DevOps sollte niemals Selbstzweck sein.

Treten wir einen Schritt zurück und betrachten das große Ganze. Da Schlagwörter wie **DevOps** und **DevSecOps** immer mehr zum Mainstream werden, sind viele Unternehmen — insbesondere solche, die eine digitale Transformation durchlaufen — schnell dabei, sie zu übernehmen. Und obwohl es unzählige glänzende Erfolgsgeschichten gibt, verfehlen viele das **Kernziel**: **die Wertlieferung zu beschleunigen und dabei hohe Qualität und Zuverlässigkeit beizubehalten.**

Stattdessen hören wir Dinge wie:

> *„Wir haben eine CI/CD-Pipeline aufgebaut. Wir machen 10 Produktions-Releases am Tag. Wir praktizieren vollständig DevOps!"*

Aber DevOps sollte niemals Selbstzweck sein.

Vor einigen Jahren leitete ich die Definition und Messung von DevOps-KPIs auf Unternehmensebene. Natürlich begann ich mit den **[4 Schlüsselmetriken](https://dora.dev/guides/dora-metrics-four-keys/)** (Deployment-Häufigkeit, Vorlaufzeit, Änderungsfehlerrate und MTTR). Aber die erste Frage des Managements überraschte mich:

> *„Hey, können wir unsere Deployment-Häufigkeit erhöhen? Ich muss meinem Chef 100 Deployments pro Monat berichten."*

![Agile-Comic](../assets/comic-agile.webp)

Das verfehlte den Punkt völlig.

Am Ende verbrachte ich einen Monat damit zu erklären, wie man **Metriken fair und sinnvoll einsetzt**. Diese Metriken sollen die **Leistung** eurer DevOps-Praktiken **widerspiegeln** — nicht zu einem Ziel werden, das man manipuliert. Man kann sie verbessern, indem man die CI/CD-Pipeline optimiert, bessere Test-Gates einführt, Trunk-based Development einführt und vieles mehr. Aber 100 Deployments nur um einer Zahl willen? Das ist nur Lärm.

Noch schlimmer: Ich habe erlebt, wie Teams rein auf Basis von Deployment-Zahlen miteinander verglichen wurden.

> *„Warum hat die Gateway-Anwendung diesen Monat nur einmal released, während der API-Service diese Woche 10 Mal released hat?"*

Diese Art von Druck führt oft zu sinnlosen Releases — nur um nicht hinterfragt zu werden. Ich habe Teams erlebt, die Code ohne echte Änderungen pushen, nur um „aktiv" zu erscheinen. Und was ist das Ergebnis? Burnout, verschwendete Mühe und erhöhtes Risiko.

Das führt uns zu einem tieferen Problem: **Werkzeuge missbrauchen, ohne ihre Kosten zu verstehen**. Als ich einem neuen Projekt beitrat, fiel mir sofort auf, dass unsere gemeinsame Jenkins-Instanz ständig überlastet war. Es stellte sich heraus, dass Dutzende von Teams tägliche Builds darauf ausführten — darunter viele unnötige oder blockierte Pipelines. Einige hatten sogar manuelle Genehmigungsschritte **ohne Timeout**. Das verbesserte nicht die Liefereffizienz — es blockierte alle anderen.

Es gibt viele großartige technische Lösungen da draußen, und DevOps ist sicherlich eine davon. Aber wie alles andere in der Technik **funktioniert es nur, wenn es richtig eingesetzt wird** — und mit der richtigen Absicht. DevOps ist genauso wichtig wie eure Produktarchitektur und genauso leicht falsch anwendbar.

Es gibt bereits unzählige Tutorials zur Implementierung von CI/CD-Pipelines. Aber **der wichtigste Teil ist die Denkweise** — wie wir zusammenarbeiten, wie wir uns verbessern und wie wir Wert liefern.

**Bei DevOps geht es nicht darum, Metriken zu jagen oder einfach nur Tools zu implementieren.**
Es geht darum, **eine Kultur zu fördern** — eine Kultur der Zusammenarbeit, des kontinuierlichen Lernens und der Lieferung echten Mehrwerts für Kunden mit Qualität und Geschwindigkeit. Ohne die richtige Denkweise und den richtigen Zweck werden selbst die besten Tools und Prozesse bedeutungslos.

**Echtes DevOps treibt Teams an, nahtlos zusammenzuarbeiten, sich ständig zu verbessern und sich auf das zu konzentrieren, was wirklich zählt — Probleme lösen und Wirkung erzielen.**
