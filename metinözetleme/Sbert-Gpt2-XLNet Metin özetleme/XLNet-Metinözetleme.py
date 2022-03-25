from summarizer import Summarizer,TransformerSummarizer
import time

start = time.time()
body ="""Front-line workers are getting some of the tech (and tracking) of office workers

Front-line workers responsible for keeping the world running during the pandemic may soon have more access to some of the same tech tools and resources that have been available for office workers. But be aware: There could be some tracking in store.
Microsoft on Wednesday unveiled several new workplace tools aimed at improving communication, collaboration and access to company resources for workers who prepare our food, operate manufacturing lines and treat sick patients. For example, front-line workers can communicate with co-workers and other departments by using a walkie-talkie app on Microsoft’s communication platform Teams that’s downloadable on iOS devices to get safety alerts at a construction site. Similarly, they can use the walkie-talkie app with the press of a button on a Zebra Technologies mobile computing and scanning device to track down items in a store. Workers can also access and streamline time-off requests on Teams through new third-party software integrations. They can access schedules and wait times for medical virtual visits. And workers will be able to access company resources like payroll as well as educational and training tools all through the same system.
Microsoft says its new releases are based on the company’s recent research, which surveyed 9,600 front-line workers and their supervisors in eight industries ranging from automotive to health care and manufacturing. The survey showed that front-line workers want to feel more valued and connected to their company’s culture and leadership. The research also suggests that workers believe tech could reduce workplace stress and is an area where they haven’t had enough access to training.
“Our research still tells us that a third of all front-line workers were saying they still don’t have the tech they need,” said Emma Williams, Microsoft’s corporate vice president of Modern Workplace Transformation. “A happy and productive front line means a better business bottom line.”
The rollout comes as Microsoft doubles down on its investment in tools for front-line workers — a group that typically takes a back seat to desk workers when it comes to investments in workplace collaboration tools. Microsoft first released its front-line-worker-focused product in 2017 with a subscription of its office software, Microsoft 365. It has since been expanding the products available to front-line workers because it sees a big market opportunity. An estimated 2.7 billion workers representing nearly 80 percent of the global workforce are considered front-line workers, according to market research firm Gartner.
“It’s a huge market,” said Leif-Olof Wallin, research vice president within mobile and wireless communications at Gartner. “In 2025, we expect front-line workers to get 75 percent of new mobile initiative investments.”
Workers at San Francisco-based Suffolk Construction, furniture fittings manufacturer Blum and energy company Chevron are already using some of Microsoft’s latest collaboration and communications tools for its workers. And while the software has helped the early adopters with tasks like boots-on-the-ground coordination and connecting employees to valuable information, workers should also be aware of the implications of the new capabilities, said Adam Seth Litwin, associate professor at Cornell University’s School of Industrial and Labor Relations.
By putting more devices and technology into the pockets and hands of front-line users, employers may also have new ways to track their employees and what they do during the day, Litwin said. For example, if employees are using new software, could their bosses know how many times they chatted with a co-worker? Would they be able to track how much time the employee spent in which apps, and how they use that information?

Microsoft said Viva, its employee resources platform that can track workers’ activities on the the company’s apps, offers “privacy-protected insights and recommendations to improve productivity and well-being.” But individual workers are the only people who will see their own personalized data. Managers and companies only receive access to anonymized, aggregated data, it said.
Litwin said workers should be cautious, and employers should prioritize tech that helps workers do their jobs.
“The idea that workers want constant information while they’re working — it’s hard for me to imagine that’s something they’ll benefit from,” Litwin said. “But if you can give workers real-time information that will help them better serve customers, I’m all for that.”
While Microsoft has been building partnerships with software companies such as Zebra Technologies, Workday and SAP to provide access to scheduling, payroll and training resources, the Big Tech company will probably need to expand its list of partners to make its products attractive to a larger number of employers, Wallin said. That means linking up with more software providers that big retail chains, hospitals and manufacturers use for workforce management.
Microsoft says it also has a partnership with Kronos, one of the largest providers of human resources software.
Still, analysts say given the massive market opportunity, mounting pressure on workers and the continuous struggle for employers to attract and retain talent, it’s only a matter of time before more technologies swarm the space. Wallin said he could easily see a situation in which Facebook starts tailoring a special version of its workplace apps for front-line workers. And Mark Moerdler, senior analyst at research firm AB Bernstein, said Google and Salesforce could also be big competitors.
Google already debuted a version of its workplace software, called Google Workspace, for front-line workers early last year. Retailers, for example, can train new hires with its videoconferencing app Google Meet or use its collaborative word document app Google Docs. It helps manufacturers build quality-control checklists with online-form builder Google Forms. And health-care workers can share digital copies of X-rays and CT scans through Google Drive.
Facebook’s parent company Meta said its software called Workplace is already used by front-line workers at Starbucks, Walmart and Virgin Atlantic. The communication tool allows workers to access it via any mobile device to chat, stream or watch live videos and create groups.
Salesforce wasn’t immediately available for comment.
When it comes to any workplace tool, Litwin said the biggest focus should be the worker not the employer.
“In a world in which workers have the power, a big part of what software vendors are going to need to do is think about work from employees’ perspective,” he said.
"""

model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
full = ''.join(model(body, min_length=60))
print(full)
end1 = time.time()
süre=end1 - start
print("Özetleme süresi",süre) 

satırlar=body.splitlines()#satırlarına ayırma
b=0#keimesatisinı tutmak için değişken
for i in satırlar:
    kelimeler=i.split()
    for a in kelimeler:
        b=b+1
print(b)

ösatırlar=full.splitlines()#satırlarına ayırma
c=0#keimesatisinı tutmak için değişken
for i in ösatırlar:
    kelimeler=i.split()
    for a in kelimeler:
        c=c+1
print(c)
        

özet_oran=100-((c/b)*100)
print("XLNet Özetleme yüzdesi:",özet_oran)
