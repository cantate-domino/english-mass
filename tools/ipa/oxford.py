# Oxford Learner's Dictionaries, British English; strong forms of function words. Keys = word with letters only.
SKIP = {'we', 'a', 'to', 'are', 'i', 'my', 'me', 'be', 'so', 'go', 'he', 'no'}
OX = {
 # function words
 'we':'wiː','a':'ə','to':'tuː','are':'ɑː(r)','i':'aɪ','my':'maɪ','me':'miː','be':'biː','so':'səʊ','go':'ɡəʊ','he':'hiː','no':'nəʊ',
 'the':'ðə','of':'ɒv','and':'ænd','for':'fɔː(r)','our':'ˈaʊə(r)','your':'jɔː(r)','you':'juː','at':'æt','in':'ɪn','on':'ɒn',
 'it':'ɪt','is':'ɪz','as':'æz','with':'wɪð','from':'frɒm','this':'ðɪs','thy':'ðaɪ','thee':'ðiː','ye':'jiː','o':'əʊ','oh':'əʊ',
 'us':'ʌs','but':'bʌt','nor':'nɔː(r)','up':'ʌp','whom':'huːm','where':'weə(r)','will':'wɪl','could':'kʊd','all':'ɔːl',
 # Blest Are You, Lord
 'blest':'blest','lord':'lɔːd','god':'ɡɒd','creation':'kriˈeɪʃn','thanks':'θæŋks','goodness':'ˈɡʊdnəs','bread':'bred',
 'offer':'ˈɒfə(r)','fruit':'fruːt','earth':'ɜːθ','work':'wɜːk','hands':'hændz','become':'bɪˈkʌm','life':'laɪf','wine':'waɪn',
 'cup':'kʌp','joy':'dʒɔɪ','blessed':'ˈblesɪd','bless':'bles','forever':'fərˈevə(r)','amen':'ɑːˈmen','men':'men',
 # Immaculate Mother
 'immaculate':'ɪˈmækjələt','mother':'ˈmʌðə(r)','come':'kʌm','call':'kɔːl','low':'ləʊ','altar':'ˈɔːltə(r)','before':'bɪˈfɔː(r)',
 'fall':'fɔːl','ave':'ˈɑːveɪ','grief':'ɡriːf','temptation':'tempˈteɪʃn','pain':'peɪn',"we'll":'wiːl','seek':'siːk','vain':'veɪn',
 'pray':'preɪ','church':'tʃɜːtʃ','upon':'əˈpɒn','sweetest':'ˈswiːtɪst','lady':'ˈleɪdi','land':'lænd','birth':'bɜːθ',
 'maria':'məˈriːə',
 # Take Our Bread
 'take':'teɪk','ask':'ɑːsk','hearts':'hɑːts','love':'lʌv','lives':'laɪvz','father':'ˈfɑːðə(r)','yours':'jɔːz','stand':'stænd',
 'table':'ˈteɪbl','set':'set','eat':'iːt',"can't":'kɑːnt','forget':'fəˈɡet','sign':'saɪn','yet':'jet','holy':'ˈhəʊli',
 'people':'ˈpiːpl','standing':'ˈstændɪŋ','washed':'wɒʃt','blood':'blʌd','spirit':'ˈspɪrɪt','filled':'fɪld','hungry':'ˈhʌŋɡri',
 'await':'əˈweɪt','food':'fuːd','poor':'pɔː(r)',"we've":'wiːv','brought':'brɔːt','ourselves':'ˌaʊəˈselvz','best':'best',
 # Lift Up Your Head
 'lift':'lɪft','heads':'hedz','mighty':'ˈmaɪti','gates':'ɡeɪts','behold':'bɪˈhəʊld','king':'kɪŋ','glory':'ˈɡlɔːri','waits':'weɪts',
 'city':'ˈsɪti','christ':'kraɪst','ruler':'ˈruːlə(r)','confest':'kənˈfest','fling':'flɪŋ','wide':'waɪd','portals':'ˈpɔːtlz',
 'heart':'hɑːt','make':'meɪk','temple':'ˈtempl','apart':'əˈpɑːt',"sov'reign":'ˈsɒvrɪn','enter':'ˈentə(r)','let':'let','new':'njuː',
 'nobler':'ˈnəʊblə(r)','begin':'bɪˈɡɪn','kings':'kɪŋz','drawing':'ˈdrɔːɪŋ','near':'nɪə(r)','savior':'ˈseɪvjə(r)','world':'wɜːld',
 'here':'hɪə(r)','happy':'ˈhæpi','homes':'həʊmz','triumph':'ˈtraɪʌmf','comes':'kʌmz','earthly':'ˈɜːθli','use':'juːs',
 "heav'n's":'hevnz','employ':'ɪmˈplɔɪ','adorned':'əˈdɔːnd','prayer':'preə(r)','guide':'ɡaɪd','until':'ənˈtɪl',
 'glorious':'ˈɡlɔːriəs','crown':'kraʊn','won':'wʌn',
 # Waiting in Silence
 'waiting':'ˈweɪtɪŋ','silence':'ˈsaɪləns','hope':'həʊp','long':'lɒŋ','trust':'trʌst','truth':'truːθ','thirst':'θɜːst',
 'ever':'ˈevə(r)','emmanuel':'ɪˈmænjuəl','jesus':'ˈdʒiːzəs','sun':'sʌn','justice':'ˈdʒʌstɪs','true':'truː','prince':'prɪns',
 'peace':'piːs','wisdom':'ˈwɪzdəm','incarnate':'ɪnˈkɑːnət','teach':'tiːtʃ','way':'weɪ','show':'ʃəʊ','path':'pɑːθ',
 'maranatha':'ˌmærəˈnɑːθə','key':'kiː','david':'ˈdeɪvɪd','open':'ˈəʊpən','give':'ɡɪv','vision':'ˈvɪʒn','flower':'ˈflaʊə(r)',
 'jesse':'ˈdʒesi','bloom':'bluːm','midst':'mɪdst','garden':'ˈɡɑːdn',
 # Hail, Holy Queen
 'hail':'heɪl','queen':'kwiːn','enthroned':'ɪnˈθrəʊnd','above':'əˈbʌv','mercy':'ˈmɜːsi','sweetness':'ˈswiːtnəs',
 'below':'bɪˈləʊ','sorrow':'ˈsɒrəʊ','when':'wen','breath':'breθ','leaves':'liːvz','son':'sʌn','sing':'sɪŋ',
 'cherubim':'ˈtʃerəbɪm','seraphim':'ˈserəfɪm','woe':'wəʊ',"heav'n":'hevn','resound':'rɪˈzaʊnd','hymn':'hɪm',
 'salve':'ˈsɑːlveɪ','regina':'reɪˈdʒiːnə',
 # All the Ends of the Earth
 'ends':'endz','creatures':'ˈkriːtʃəz','sea':'siː','eyes':'aɪz','wonders':'ˈwʌndəz','master':'ˈmɑːstə(r)','has':'hæz',
 'world':'wɜːld','break':'breɪk','into':'ˈɪntuː','song':'sɒŋ','deeds':'diːdz','done':'dʌn',"ev'ry":'ˈevri','age':'eɪdʒ',
 'heaven':'ˈhevn','shall':'ʃæl','re':'rɪ','joice':'dʒɔɪs','his':'hɪz','might':'maɪt','nation':'ˈneɪʃn','him':'hɪm',
 'made':'meɪd','salvation':'sælˈveɪʃn','known':'nəʊn','faithful':'ˈfeɪθfl','prom':'ˈprɒm','ises':'ɪsɪz','old':'əʊld',
 'holds':'həʊldz','music':'ˈmjuːzɪk',
}
