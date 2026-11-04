/* English Mass · St. Joseph Convent – the TEXTS of each Mass (shown on index.html)
   The songs and sung Mass parts are NOT here: they come from data.js, shared with the song page (songs.html),
   so a song changed there changes on both pages.

   One entry per date ("YYYY-MM-DD"), the same date as in data.js. Fields (all optional):
     title     = celebration, if data.js has no feast for that date (names follow the Dominican calendar, "Lich Phung vu OP")
     note      = rank or options, shown after the title: "Feast", "Memorial", "Optional memorial: …"
     universal = true / false: Universal Prayer shown or not (default: Sundays only)
     color     = "green" | "white" | "red" | "violet"
     time      = "05:30" (shown beside the date)
     gloria, creed = true when prescribed
     readings  = [first, psalm, second?] – each { kind, cite, incipit_en?, refrain_en? (psalm), chunks: [["", text], …] }
                 or { kind, cite, tba: true } while the text is not yet entered
     alleluia  = { cite, text }            (the verse; the sung Alleluia itself comes from data.js mass.alleluia)
     gospel    = { evangelist, cite, chunks } or { evangelist, cite, tba: true }
     ea, ca    = Entrance / Communion Antiphon [[text, cite]]   (hidden unless "Rubrics" is switched on)
     collect, po (Prayer over the Offerings), pc (Prayer after Communion) = full text; left out → "… of the day · Roman Missal"
     preface_en = name of the Preface; prefaces = [[name, full text]]
     pf        = Universal Prayer { intro_en, resp_en, items: [{ en }], close_en }; pfBook = [note]
     lyrics    = { entrance: "…", … } words shown under a song title (optional)
   Readings: English text of the Lectionary (USCCB); propers: The Roman Missal (2011). Change SITE.updated in data.js after every edit. */
window.TEXTS = {
  "2026-11-01": {
    color: "white", time: "05:30", gloria: true, creed: true,
    ea: [["Let us all rejoice in the Lord,\nas we celebrate the feast day in honor of all the Saints,\nat whose festival the Angels rejoice\nand praise the Son of God.", ""]],
    collect: "Almighty ever-living God,\nby whose gift we venerate in one celebration\nthe merits of all the Saints,\nbestow on us, we pray,\nthrough the prayers of so many intercessors,\nan abundance of the reconciliation with you\nfor which we earnestly long.\nThrough our Lord Jesus Christ, your Son,\nwho lives and reigns with you in the unity of the Holy Spirit,\none God, for ever and ever.",
    readings: [
      {"kind": "first", "cite": "Revelation 7:2-4, 9-14", "cite_vi": "Kh 7,2-4.9-14", "lang": "EN", "incipit_en": "A reading from the Book of Revelation", "chunks": [["", "I, John, saw another angel come up from the East,\nholding the seal of the living God.\nHe cried out in a loud voice to the four angels\nwho were given power to damage the land and the sea,\n“Do not damage the land or the sea or the trees\nuntil we put the seal on the foreheads of the servants of our God.”\nI heard the number of those who had been marked with the seal,\none hundred and forty-four thousand marked\nfrom every tribe of the children of Israel.", ""], ["", "After this I had a vision of a great multitude,\nwhich no one could count,\nfrom every nation, race, people, and tongue.\nThey stood before the throne and before the Lamb,\nwearing white robes and holding palm branches in their hands.\nThey cried out in a loud voice:", ""], ["", "“Salvation comes from our God, who is seated on the throne,\nand from the Lamb.”", ""], ["", "All the angels stood around the throne\nand around the elders and the four living creatures.\nThey prostrated themselves before the throne,\nworshiped God, and exclaimed:", ""], ["", "“Amen. Blessing and glory, wisdom and thanksgiving,\nhonor, power, and might\nbe to our God forever and ever. Amen.”", ""], ["", "Then one of the elders spoke up and said to me,\n“Who are these wearing white robes, and where did they come from?”\nI said to him, “My lord, you are the one who knows.”\nHe said to me,\n“These are the ones who have survived the time of great distress;\nthey have washed their robes\nand made them white in the Blood of the Lamb.”", ""]]},
      {"kind": "psalm", "cite": "Psalm 24:1bc-2, 3-4ab, 5-6", "cite_vi": "Tv 23,1bc-2.3-4ab.5-6", "lang": "EN", "refrain_en": "Lord, this is the people that longs to see your face.", "chunks": [["", "The LORD’s are the earth and its fullness;\nthe world and those who dwell in it.\nFor he founded it upon the seas\nand established it upon the rivers.", ""], ["", "Who can ascend the mountain of the LORD?\nor who may stand in his holy place?\nOne whose hands are sinless, whose heart is clean,\nwho desires not what is vain.", ""], ["", "He shall receive a blessing from the LORD,\na reward from God his savior.\nSuch is the race that seeks him,\nthat seeks the face of the God of Jacob.", ""]]},
      {"kind": "second", "cite": "1 John 3:1-3", "cite_vi": "1 Ga 3,1-3", "lang": "EN", "incipit_en": "A reading from the first Letter of Saint John", "chunks": [["", "Beloved:\nSee what love the Father has bestowed on us\nthat we may be called the children of God.\nYet so we are.\nThe reason the world does not know us\nis that it did not know him.\nBeloved, we are God’s children now;\nwhat we shall be has not yet been revealed.\nWe do know that when it is revealed we shall be like him,\nfor we shall see him as he is.\nEveryone who has this hope based on him makes himself pure,\nas he is pure.", ""]]}
    ],
    alleluia: { cite: "Matthew 11:28", text: "Come to me, all you who labor and are burdened, and I will give you rest, says the Lord." },
    gospel: {"evangelist": "Matthew", "kind": "gospel", "cite": "Matthew 5:1-12a", "cite_vi": "Mt 5,1-12a", "lang": "EN", "chunks": [["", "When Jesus saw the crowds, he went up the mountain,\nand after he had sat down, his disciples came to him.\nHe began to teach them, saying:", ""], ["", "“Blessed are the poor in spirit,\nfor theirs is the Kingdom of heaven.\nBlessed are they who mourn,\nfor they will be comforted.\nBlessed are the meek,\nfor they will inherit the land.\nBlessed are they who hunger and thirst for righteousness,\nfor they will be satisfied.\nBlessed are the merciful,\nfor they will be shown mercy.\nBlessed are the clean of heart,\nfor they will see God.\nBlessed are the peacemakers,\nfor they will be called children of God.\nBlessed are they who are persecuted for the sake of righteousness,\nfor theirs is the Kingdom of heaven.\nBlessed are you when they insult you and persecute you\nand utter every kind of evil against you falsely because of me.\nRejoice and be glad,\nfor your reward will be great in heaven.”", ""]]},
    pfBook: ["Intentions prepared by the community."],
    po: "May these offerings we bring in honor of all the Saints\nbe pleasing to you, O Lord,\nand grant that, just as we believe the Saints\nto be already assured of immortality,\nso we may experience their concern for our salvation.\nThrough Christ our Lord.",
    preface_en: "Preface: The glory of Jerusalem, our mother",
    prefaces: [["Preface: The glory of Jerusalem, our mother", "It is truly right and just, our duty and our salvation,\nalways and everywhere to give you thanks,\nLord, holy Father, almighty and eternal God.\nFor today by your gift we celebrate the festival of your city,\nthe heavenly Jerusalem, our mother,\nwhere the great array of our brothers and sisters\nalready gives you eternal praise.\nTowards her, we eagerly hasten\nas pilgrims advancing by faith,\nrejoicing in the glory bestowed upon\nthose exalted members of the Church\nthrough whom you give us, in our frailty,\nboth strength and good example.\nAnd so, we glorify you with the multitude\nof Saints and Angels,\nas with one voice of praise we acclaim:"]],
    ca: [["Blessed are the clean of heart, for they shall see God.\nBlessed are the peacemakers,\nfor they shall be called children of God.\nBlessed are they who are persecuted for the sake of righteousness,\nfor theirs is the Kingdom of Heaven.", "Mt 5: 8-10"]],
    pc: "As we adore you, O God, who alone are holy\nand wonderful in all your Saints,\nwe implore your grace,\nso that, coming to perfect holiness\nin the fullness of your love,\nwe may pass from this pilgrim table\nto the banquet of our heavenly homeland.\nThrough Christ our Lord.",
    lyrics: {"entrance": "Refrain:\nAll the ends of the earth,\nall you creatures of the sea,\nlift up your eyes to the wonders of the Lord.\nFor the Lord of the earth,\nthe master of the sea,\nhas come with justice for the world.\n\n1. Break into song at the deeds of the Lord,\nthe wonders God has done in ev'ry age.\n\n2. Heaven and earth shall rejoice in his might\nev'ry heart ev'ry nation call him Lord.", "offertory": "Refrain:\nSeed, scattered and sown,\nwheat, gathered and grown,\nbread, broken and shared as one,\nthe Living bread of God.\nVine, fruit of the land, wine,\nwork of our hands, one cup that is\nshared by all; the Living Cup,\nthe Living Bread of God.\n\n1. Is not the bread we break,\nA sharing in our Lord?\nIs not the cup we bless,\nthe blood of Christ outpoured?\n\n2. The seed which falls on rock\nwill wither and will die,\nThe seed within good ground\nwill flower and have life.", "communion": "1. Christians, let us love one another,\nas we share the true living bread.\nJesus is our God and our brother;\nwith his flesh and blood we are fed\n\nRefrain:\nEveryone who loves is born of God.\nJesus is our life, God is love.\n\n2. We who break this bread are one body,\nwe who share this cup are all one,\nchildren of our Father in heaven,\nsharers of the life of God's Son.\n\n3. We who eat and drink at this table\ndie and rise again with our Lord,\ndrawing from our rock living water\nfor all men who thirst for accord.", "recessional": "Refrain:\nA song on my lips with love in my heart,\nI go my merry way.\nThe sun in my eyes, the sun in my heart\nlights up my steps from day to day.\n\n4. Then we'll all be reunited,\nsinging one eternal chord,\nfor we know we've been invited\nto the mansion of the Lord."}
  },
  /* Sat 7 Nov: All Saints of the Order of Preachers, Feast (Dominican calendar) – Proper of the Order: texts to be entered */
  "2026-11-07": {
    note: "Feast", color: "white", gloria: true,
    readings: [ { kind: "first", tba: true }, { kind: "psalm", tba: true } ],
    gospel: { evangelist: "Mark", cite: "Mark 10:28-30", tba: true }
  },
  /* Sat 14 Nov: Saturday of the 32nd Week in Ordinary Time (Year II). Optional: Bl. John Liccio, Bl. Lucy of Narni (OP), or the BVM on Saturday */
  "2026-11-14": {
    title: "Saturday of the Thirty-second Week in Ordinary Time", color: "green",
    note: "Optional memorial: Bl. John Liccio, Priest, and Bl. Lucy of Narni, Virgin, of our Order; or the Blessed Virgin Mary",
    readings: [ { kind: "first", cite: "3 John 5-8", tba: true }, { kind: "psalm", cite: "Psalm 112:1-2, 3-4, 5-6", tba: true } ],
    gospel: { evangelist: "Luke", cite: "Luke 18:1-8", tba: true }
  },
  /* Sat 21 Nov: The Presentation of the Blessed Virgin Mary, Memorial */
  "2026-11-21": {
    title: "The Presentation of the Blessed Virgin Mary", note: "Memorial", color: "white",
    readings: [ { kind: "first", cite: "Zechariah 2:14-17", tba: true }, { kind: "psalm", cite: "Luke 1:46-47, 48-49, 50-51, 52-53, 54-55", tba: true } ],
    gospel: { evangelist: "Matthew", cite: "Matthew 12:46-50", tba: true }
  },
  /* Sat 28 Nov: Saturday of the 34th Week in Ordinary Time (Year II); by the custom of the Order a free Saturday is the
     Memorial of the BVM (calendar: "Hoặc lễ về Đức Trinh Nữ Maria"; note 4 of the calendar) */
  "2026-11-28": {
    title: "Saturday Memorial of the Blessed Virgin Mary", note: "Saturday of the 34th Week in Ordinary Time", color: "white",
    readings: [ { kind: "first", cite: "Revelation 22:1-7", tba: true }, { kind: "psalm", cite: "Psalm 95:1-2, 3-5, 6-7ab", tba: true } ],
    gospel: { evangelist: "Luke", cite: "Luke 21:34-36", tba: true }
  }
};
