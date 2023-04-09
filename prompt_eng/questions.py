import re

def init():
	questions = {
		'Data Security' : {
			'question-bullets' : \
				"""
				- How is my data protected by both parties?
				- What are the differences in how each policy claims to protect my data?
				- Do either of these policies make mention of what they do in the event of a data breach?
				- Do either of these policies place any restrictions on the user for security purposes?
				""",
			'question-paragraph' : \
				"""
				I have some questions about these policies. First, I want to know how these policies are the same and how they differ. Could you tell me how my data is protected by both parties? What about the differences in how each policy claims to protect my data? Additionally, data breaches seem to be a big issue. Do either of these policies make mention of what they do in the event of one? Finally, Do either of these policies place any restrictions on the user for security purposes?
				""",
			'instruction-bullets' : \
				"""
				- Tell me how both policies protect my data.
				- Identify how each policiy is different in how they protect my data.
				- Tell me if these policies talk about what their respective companies do in the event of a data breach.
				- List out any restrictions that are placed on the user for the purpose of security.
				""",
			'instruction-paragraph' : \
				"""
				Answer the following. I want to compare the two documents so first tell me the similarities and the differences in how each policy protects my data. Next, Tell me if either of these policies make mention of what they do in the event of a data breach. Finally, tell me if either of these policies place any restrictions on the user for security purposes.
				""",
		},
		'Data Retention' : {
			'question-bullets' : \
				"""
				- What kind of data is collected by both policies?
				- What kind of data is exclusively collected by each policy?
				- Can I opt out of having my data collected by any of these policies?
				- Do either of these companies make mention of how long they retain data for?
				""",
			'question-paragraph' : \
				"""
				I have some questions about these policies. First, what kind of data is collected by both policies and what kind of data is exclusively collected by each policy? What about user consent? Can I opt out of having my data collected by any of these policies? Finally, Do either of these companies make mention of how long they retain data for?
				""",
			'instruction-bullets' : \
				"""
				- Tell me the kind of data is collected by both policies.
				- Find out what data is exclusively collected by each policy.
				- Tell me if I can opt out of having my data collected by either policy.
				- Identify any data retention periods in the policies.
				""",
			'instruction-paragraph' : \
				"""
				Answer the following. First, I want to compare these policies so tell me similarities and differences in how each of them collect my data. Now I want to know if I have a choice when using their services so tell me if I can opt out of having my data collected by either policy. Finally, tell me if either policy mentions a data retention period and what that retention period is.
				""",
		},
		'Third Party Sharing/Collection' : {
			'question-bullets' : \
				"""
				- Enumerate the third party entities that will have access to my data?
				- What are the third parties that are only mentioned in one of each of the given policies?
				- Do any of these policies make any distinction between what data is and isn't shared?
				""",
			'question-paragraph' : \
				"""
				I have some questions about these policies. I want to compare these policies so tell me if you can identify the common and different third party entities that will have access to my data. The only other thing I want you to do is to tell me if any of these policies make any distinction between what data is and isn't shared.
				""",
			'instruction-bullets' : \
				"""
				- If applicable, identify the common third party entities that will have access to my data.
				- Identify the exclusive third parties that will have access to my data.
				- Tell me if either policy explicitly states that some data is not shared and if so then tell me what they are.
				""",
			'instruction-paragraph' : \
				"""
				Answer the following. I want to know how my data is being shared so if applicable, identify the common as well as the differing third party entities that will have access to my data. Then to see if there is any more granularity in their policy, tell me if either policy explicitly states that some data is not shared and if so then tell me what they are.
				""",
		},
		'User Access, Edit and Deletion' : {
			'question-bullets' : \
				"""
				- Do any of these policies prevent me from being able to change my information on my own?
				- Do any of these policies allow me to see what data is being shared?
				- If I am able to delete my account, do either of these policies mention that my data gets deleted as well?
				- Do either of these policies put a time restriction on when I can change or delete my information?
				- Do either of these policies allow me to opt out of sharing my data?
				- If either of these policies allow me to opt out of sharing my data, do they say how I can do it?
				""",
			'question-paragraph' : \
				"""
				I have some questions about these policies. I want to know how much control I have over my data and profile. With this in mind, do any of these policies prevent me from being able to change my information on my own? If I were to want to delete my account, do either of these policies mention that my data gets deleted as well? Do either of these policies put any time restrictions on when I can change or delete my information? Do either of these policies allow me to opt out of sharing my data at all? If either of these policies allow me to opt out of sharing my data, do they say how I can do it? Do any of these policies allow me to see what data is being shared?
				""",
			'instruction-bullets' : \
				"""
				- Identify if any of these policies prevent me from being able to change my information on my own.
				- Tell me if either company is transparent about what data of mine is being shared.
				- Tell me if either service allows me to delete my account and whether my data is retained if so.
				- Identify any time restrictions on when I am able to delete my data.
				- Do either of these policies allow me to opt out of sharing my data?
				- Tell me if either of these policies allow me to opt out of sharing my data and if so then how.
				""",
			'instruction-paragraph' : \
				"""
				Answer the following. I would like to know how much control I have over my own data so please identify if any of these policies prevent me from being able to change my information on my own. For that same reason I want to know if either service allows me to delete my account and whether my data is retained if so. Identify any time restrictions on when I am able to delete my data. I would also like to know if either of these policies allow me to opt out of sharing my data. Lastly, tell me if either company is transparent about what data of mine is being shared.  
				""",
		},
		'First Party Collection/Use' : {
			'question-bullets' : \
				"""
				- Do either of these policies mention what my data is used for?
				- Do either of these policies mention what my data is not used for?
				- Do any of these policies share my data and if so do they mention who?
				- Do either these policies specify what data is collected and if so what are they?
				- Do either of these policies allow me to opt out of having my data collected or shared ?
				""",
			'question-paragraph' : \
				"""
				I have some questions about these policies. Of course data is being collected but do either these policies specify what kind of data is collected and if so what are they? Do either of these policies mention what the companies use and do not use my data for? Could you also tell me if any of these policies share my data and if so do they mention who? Do either of these policies allow me to opt out of having my data collected or shared ?
				""",
			'instruction-bullets' : \
				"""
				- If it is covered, enumerate the ways in which my data is used for by both policies.
				- If covered, list the ways in which my data is not used by both policies.
				- For these policies, list any mentioned entity who will have access to my data.
				- Identify what data is collected by each policy.
				- Tell me if these policies allow me to opt out of having my data collected or shared.
				""",
			'instruction-paragraph' : \
				"""
				If it is covered, enumerate the ways in which my data is used for by both policies. If covered, list the ways in which my data is not used by both policies. For these policies, list any mentioned entity who will have access to my data. Identify what data is collected by each policy. Tell me if these policies allow me to opt out of having my data collected or shared
				""",
		}, 
		'User Choice/Control' : {
			'question-bullets' : \
				"""
				- Do either of these policies allow me to decide what data of mine is and isn't collected?
				- If applicable do either of these policies mention if I am able to opt out of having my private data shared to third parties?
				- If I am able to opt out of any of these services, do the policies lay out the proecedure for doing so?
				""",
			'question-paragraph' : \
				"""
				I have some questions about these policies. Could you tell me if either of these policies allow me to decide what data of mine is and isn't collected? If I am not comfortable with my data being shared to third parties but still want to use their services do either of these policies mention if I am able to opt out from sharing my data? And lastly, if I am able to opt out of any of these services, do the policies lay out the proecedure for doing so?
				""",
			'instruction-bullets' : \
				"""
				- Tell me if either of these policies allow me to decide what data of mine is and isn't collected.
				- Idententify whether I am able to opt out of having my private data shared to third parties for either policy.
				- If I am able to opt out of any of these services, please read to me the the proecedure for doing so.
				""",
			'instruction-paragraph' : \
				"""
				I would prefer to not share my data so please tell me if either of these policies allow me to decide what data of mine is and isn't collected. Additionally, please idententify whether I am able to opt out of having my private data shared to third parties for either policy. Finally, if I am able to opt out of any of these services, please read to me the the proecedure for doing so.
				""",
		},
		'Other' : {
			'question-bullets' : \
				"""
				- What do either of these policies say about how they handle third party cookies?
				""",
			'question-paragraph' : \
				"""
				What do either of these policies say about how they handle third party cookies?
				""",
			'instruction-bullets' : \
				"""
				- Tell me what these policies say about how they handle third party cookies.
				""",
			'instruction-paragraph' : \
				"""
				Tell me what these policies say about how they handle third party cookies.
				""",
		},
		'International and Specific Audiences' : {
			'question-bullets' : \
				"""
				- Do either of these policies mention any special considerations regarding users of specific states or countries?
				- If appliciable, what countries or states are given special consideration in any of these policies?
				""",
			'question-paragraph' : \
				"""
				I am not sure if this applies to me but do either of these policies mention any special considerations regarding users of specific states or countries? If so then what countries or states are given special consideration and by which policy?
				""",
			'instruction-bullets' : \
				"""
				- Tell me any special considerations regarding users of specific states or countries.
				- List the countries or states are given special consideration in any of these policies.
				""",
			'instruction-paragraph' : \
				"""
				Follow these instructions. Tell me any special considerations regarding users of specific states or countries. If any considerations are stated, please list the countries or states are given special consideration in any of these policies.
				""",
		},
		'Policy Change' : {
			'question-bullets' : \
				"""
				- Do either of these policies mention where I would need to go to see if there have been any updates?
				- Do either of these policies make note that their companies actively notify their users when there is a change in the policy?
				- How will either of these policies let me know if there has been a change to the policy?
				""",
			'question-paragraph' : \
				"""
				I have some questions about these policies. I am curious as to what would happen in the event of an update to the policy so do either of them mention where I would need to go to see if there have been any updates? And how would I know if there has been a recent change? do either of these policies make note that their companies actively notify their users when there is a change in the policy? In what way would they let me know if there has been any changes?
				""",
			'instruction-bullets' : \
				"""
				- Tell me where I would need to go to see if there have been any updates to either of these policies.
				- Identify whether I would be of notified of an update to either policy in a timely matter.
				- Tell me how I would be notified if there has been a change to either policy.
				""",
			'instruction-paragraph' : \
				"""
				Follow these instructions. Tell me where I would need to go to see the changes to either of these policies in the event that an update has taken place. Additionally please identify whether I would be of notified of an update in a timely matter and how they would send the notification.
				""",
		},
	}

	for category in questions.keys():
		for style in questions[category].keys():
			questions[category][style] = re.sub(
				'\n *',
				'\n',
				questions[category][style]
			)
			questions[category][style] = re.sub(
				'\n\t*',
				'\n',
				questions[category][style]
			)
	return questions
