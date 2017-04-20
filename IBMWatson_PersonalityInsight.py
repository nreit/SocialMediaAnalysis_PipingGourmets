import requests
import json
import pandas as pd



nameofCSVFileWithTweets = "PipingGourmets.csv"


df = pd.DataFrame.from_csv(nameofCSVFileWithTweets, index_col=None)
tweets = df['TweetText']
fileTXT = open('tweetText.txt', 'wb')
tweets.to_csv(fileTXT, sep=' ', index=False, header=False)
fileTXT.close()


with open('tweetText.txt', 'r') as myfile:
		tweets = myfile.read()


# https://github.com/watson-developer-cloud/python-sdk
username = "INPUT IBM BLUEMIX USERNAME CREDENTIALS HERE"
password = "INPUT IBM BLUEMIX PASSWORD CREDENTIALS HERE"


def analyzeTweets():

	# make the call to IBM Watson	
	response = requests.post("https://gateway.watsonplatform.net/personality-insights/api/v2/profile",
			auth=(username, password),
			headers = {"content-type": "text/plain"},
			data = tweets
         )

	jsonProfile = json.loads(response.text)

	traits = jsonProfile['tree']['children'][0]['children'][0]['children']
	#Big 5: Trait 1
	print 'IBM Watson'
	print '\n'
	print 'BIG 5 PERSONALITY:'
	print "Big 5: Personality Trait 1 - Openness"
	trait_openness = str((round((traits[0]['percentage']), 4)) * 100) + "%"
	print "OVERALL Openness: " + str(trait_openness)
	#Specific
	trait_adventurousness = str((round((traits[0]['children'][0]['percentage']), 4)) * 100) + "%"
	print "Adventurousness: " + str(trait_adventurousness)
	trait_artisticinterests = str((round((traits[0]['children'][1]['percentage']), 4)) * 100) + "%"
	print "Artistic Interests: " + str(trait_artisticinterests)
	trait_emotionality = str((round((traits[0]['children'][2]['percentage']), 4)) * 100) + "%"
	print "Emotionality: " + str(trait_emotionality)
	trait_imagination = str((round((traits[0]['children'][3]['percentage']), 4)) * 100) + "%"
	print "Imagination: " + str(trait_imagination)
	trait_intellect = str((round((traits[0]['children'][4]['percentage']), 4)) * 100) + "%"
	print "Intellect: " + str(trait_intellect)
	trait_authorityChallenging = str((round((traits[0]['children'][5]['percentage']), 4)) * 100) + "%"
	print "Authority Challenging: " + str(trait_authorityChallenging)
	#Big 5: Trait 2
	print '\n'
	print "Big 5: Personality Trait 2 - Conscientiousness"
	trait_conscientiousness = str((round((traits[1]['percentage']), 4)) * 100) + "%"
	print "OVERALL Conscientiousness: " + str(trait_conscientiousness)
	#Specific
	trait_achievementstriving = str((round((traits[1]['children'][0]['percentage']), 4)) * 100) + "%"
	print "Achievement Striving: " + str(trait_achievementstriving)
	trait_cautiousness = str((round((traits[1]['children'][1]['percentage']), 4)) * 100) + "%"
	print "Cautiousness: " + str(trait_cautiousness)
	trait_dutifulness = str((round((traits[1]['children'][2]['percentage']), 4)) * 100) + "%"
	print "Dutifulness: " + str(trait_dutifulness)
	trait_orderliness = str((round((traits[1]['children'][3]['percentage']), 4)) * 100) + "%"
	print "Orderliness: " + str(trait_orderliness)
	trait_selfdiscipline = str((round((traits[1]['children'][4]['percentage']), 4)) * 100) + "%"
	print "Self Discipline: " + str(trait_selfdiscipline)
	trait_selfefficacy = str((round((traits[1]['children'][5]['percentage']), 4)) * 100) + "%"
	print "Self Efficacy: " + str(trait_selfefficacy)
	#Big 5: Trait 3
	print '\n'
	print "Big 5: Personality Trait 3 - Extraversion"
	trait_extraversion = str((round((traits[2]['percentage']), 4)) * 100) + "%"
	print "OVERALL Extraversion: " + str(trait_extraversion)
	#Specific
	trait_activitylevel = str((round((traits[2]['children'][0]['percentage']), 4)) * 100) + "%"
	print "Activity Level: " + str(trait_activitylevel)
	trait_assertiveness = str((round((traits[2]['children'][1]['percentage']), 4)) * 100) + "%"
	print "Assertiveness: " + str(trait_assertiveness)
	trait_cheerfulness = str((round((traits[2]['children'][2]['percentage']), 4)) * 100) + "%"
	print "Cheerfulness: " + str(trait_cheerfulness)
	trait_excitementseeking = str((round((traits[2]['children'][3]['percentage']), 4)) * 100) + "%"
	print "Excitement Seeking: " + str(trait_excitementseeking)
	trait_friendliness = str((round((traits[2]['children'][4]['percentage']), 4)) * 100) + "%"
	print "Friendliness: " + str(trait_friendliness)
	trait_gregariousness = str((round((traits[2]['children'][5]['percentage']), 4)) * 100) + "%"
	print "Gregariousness: " + str(trait_gregariousness)
	#Big 5: Trait 4
	print '\n'
	print "Big 5: Personality Trait 4 - Agreeableness"
	trait_agreeableness = str((round((traits[3]['percentage']), 4)) * 100) + "%"
	print "OVERALL Agreeableness: " + str(trait_agreeableness)
	#Specific
	trait_altruism = str((round((traits[3]['children'][0]['percentage']), 4)) * 100) + "%"
	print "Altruism: " + str(trait_altruism)
	trait_cooperation = str((round((traits[3]['children'][1]['percentage']), 4)) * 100) + "%"
	print "Cooperation: " + str(trait_cooperation)
	trait_modesty = str((round((traits[3]['children'][2]['percentage']), 4)) * 100) + "%"
	print "Modesty: " + str(trait_modesty)
	trait_uncompromising = str((round((traits[3]['children'][3]['percentage']), 4)) * 100) + "%"
	print "Uncompromising: " + str(trait_uncompromising)
	trait_sympathy = str((round((traits[3]['children'][4]['percentage']), 4)) * 100) + "%"
	print "Sympathy: " + str(trait_sympathy)
	trait_trust = str((round((traits[3]['children'][5]['percentage']), 4)) * 100) + "%"
	print "Trust: " + str(trait_trust)
	#Big 5: Trait 5
	print '\n'
	print 'Big 5: Personality Trait 5 - Neuroticism'
	trait_neuroticism = str((round((traits[4]['percentage']), 4)) * 100) + "%"
	print "OVERALL Neuroticism: " + str(trait_neuroticism)
	#Specific
	trait_anger = str((round((traits[4]['children'][0]['percentage']), 4)) * 100) + "%"
	print "Anger: " + str(trait_anger)
	trait_anxiety = str((round((traits[4]['children'][1]['percentage']), 4)) * 100) + "%"
	print "Anxiety: " + str(trait_anxiety)
	trait_depression = str((round((traits[4]['children'][2]['percentage']), 4)) * 100) + "%"
	print "Depression: " + str(trait_depression)
	trait_immoderation = str((round((traits[4]['children'][3]['percentage']), 4)) * 100) + "%"
	print "Immoderation: " + str(trait_immoderation)
	trait_selfconsciousness = str((round((traits[4]['children'][4]['percentage']), 4)) * 100) + "%"
	print "Self Consciousness: " + trait_selfconsciousness
	trait_vulnerability = str((round((traits[4]['children'][5]['percentage']), 4)) * 100) + "%"
	print "Vulnerability: " + str(trait_vulnerability)



	print '\n \n'
	print 'NEEDS:'
	needs = jsonProfile['tree']['children'][1]['children'][0]['children']
	need_challenge = str((round((needs[0]['percentage']), 4)) * 100) + "%"
	print str(needs[0]['name']) + ": " + str(need_challenge)
	need_closeness = str((round((needs[1]['percentage']), 4)) * 100) + "%"
	print str(needs[1]['name']) + ": " + str(need_closeness)
	need_curiosity = str((round((needs[2]['percentage']), 4)) * 100) + "%"
	print str(needs[2]['name']) + ": " + str(need_curiosity)
	need_excitement = str((round((needs[3]['percentage']), 4)) * 100) + "%"
	print str(needs[3]['name']) + ": " + str(need_excitement)
	need_harmony = str((round((needs[4]['percentage']), 4)) * 100) + "%"
	print str(needs[4]['name']) + ": " + str(need_harmony)
	need_ideal = str((round((needs[5]['percentage']), 4)) * 100) + "%"
	print str(needs[5]['name']) + ": " + str(need_ideal)
	need_liberty = str((round((needs[6]['percentage']), 4)) * 100) + "%"
	print str(needs[6]['name']) + ": " + str(need_liberty)
	need_love = str((round((needs[7]['percentage']), 4)) * 100) + "%"
	print str(needs[7]['name']) + ": " + str(need_love)
	need_practicality = str((round((needs[8]['percentage']), 4)) * 100) + "%"
	print str(needs[8]['name']) + ": " + str(need_practicality)
	need_selfexpression = str((round((needs[9]['percentage']), 4)) * 100) + "%"
	print str(needs[9]['name']) + ": " + str(need_selfexpression)
	need_stability = str((round((needs[10]['percentage']), 4)) * 100) + "%"
	print str(needs[10]['name']) + ": " + str(need_stability)
	need_structure = str((round((needs[11]['percentage']), 4)) * 100) + "%"
	print str(needs[11]['name']) + ": " + str(need_structure)


	print '\n \n'
	print 'VALUES:'
	values = jsonProfile['tree']['children'][2]['children'][0]['children']
	value_conservation = str((round((values[0]['percentage']), 4)) * 100) + "%"
	print str(values[0]['name']) + ": " + str(value_conservation)
	value_opennesstochange = str((round((values[1]['percentage']), 4)) * 100) + "%"
	print str(values[1]['name']) + ": " + str(value_opennesstochange)
	value_hedonism = str((round((values[2]['percentage']), 4)) * 100) + "%"
	print str(values[2]['name']) + ": " + str(value_hedonism)
	value_selfenhancement = str((round((values[3]['percentage']), 4)) * 100) + "%"
	print str(values[3]['name']) + ": " + str(value_selfenhancement)
	value_selftranscendence = str((round((values[4]['percentage']), 4)) * 100) + "%"
	print str(values[4]['name']) + ": " + str(value_selftranscendence)



analyzeTweets()

