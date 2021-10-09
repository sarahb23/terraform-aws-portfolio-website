import json, os
from jinja2 import Environment, FileSystemLoader


class static_html_builder:
    def __init__ (self, site_data, page):
        self.site_data = site_data
        self.page = page
        self.output_file = os.getcwd() + '/public/' + page
        self.siteData = json.loads(open(self.site_data, 'r').read())
    def build(self, render_content):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(self.page)
        output = template.render(**render_content)
        with open(self.output_file, 'w') as f:
            f.write(output)
    def resume(self):
        return f'<a class="nav-link" href="/resume.html">Resume</a>'
    def profile(self):
        name = self.siteData['resumeData']['name']
        profilePicUrl = self.siteData['resumeData']['profilePicUrl']
        return f'''
        <a class="navbar-brand js-scroll-trigger" href="#page-top">
            <span class="d-block d-lg-none">{name[0]} {name[1]}</span>
            <span class="d-none d-lg-block"><img class="img-fluid img-profile rounded-circle mx-auto mb-2" src={profilePicUrl} alt="" /></span>
        </a>
        '''
    def about(self):
        name = self.siteData['resumeData']['name']
        email = self.siteData['resumeData']['email']
        socialLinks = self.siteData['resumeData']['socialLinks']
        aboutMe = self.siteData['resumeData']['aboutMe']
        return f'''
            <!-- About-->
            <section class="resume-section" id="about">
                <div class="resume-section-content">
                    <h1 class="mb-0">
                        {name[0]}
                        <span class="text-primary">{name[1]}</span>
                    </h1>
                    <div class="subheading mb-5">
                        <a href="mailto:{email}">{email}</a>
                    </div>
                    <p class="lead mb-5">{aboutMe}</p>
                    <div class="social-icons">
                        <a class="social-icon" href="{socialLinks['linkedin']['url']}"><i class="fab fa-linkedin-in"></i></a>
                        <a class="social-icon" href="{socialLinks['github']['url']}"><i class="fab fa-github"></i></a>
                    </div>
                </div>    
            </section>
            <hr class="m-0" />
        '''
    def experience(self):
        experience = ""
        for exp in self.siteData['resumeData']['work']:
            experience += f'''
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0">{exp['title']}</h3>
                <div class="subheading mb-3">{exp['companyName']}</div>
            '''
            for i in exp['responsibilities']:
                experience += f'<p>{i}</p>'
            experience += f'''
                </div>
                    <div class="flex-shrink-0"><span class="text-primary">{exp['dateStarted']} - {exp['dateUntil']}</span></div>
                </div>
            '''
        return f'''
            <!-- Experience-->
            <section class="resume-section" id="experience">
                <div class="resume-section-content">
                    <h2 class="mb-5">Experience</h2>
                        {experience}
                </div>
            </section>
            <hr class="m-0" />
        '''
    def education(self):
        education = ""
        for edu in self.siteData['resumeData']['education']:
            education += f'''
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0">{edu['universityName']}</h3>
                            <div class="subheading mb-3">{edu['degree']}</div>
                            <div>{edu['description']}</div>
                    </div>
                <div class="flex-shrink-0"><span class="text-primary">{edu['dateStarted']} - {edu['dateCompleted']}</span></div>
                </div>
            '''

        return f'''
            <!-- Education-->
            <section class="resume-section" id="education">
                <div class="resume-section-content">
                    <h2 class="mb-5">Education</h2>
                        {education}
                </div>
            </section>
            <hr class="m-0" />
        '''
    def skills(self):
        skill_data = self.siteData['resumeData']['skills']
        icons = ""
        for icon in skill_data['fontAwesomeIcons']:
            icons += f'<li class="list-inline-item"><i class="fab fa-{icon}"></i></li>'
        icons_block = f'''
            <ul class="list-inline dev-icons">
                {icons}
            </ul>
        '''
        languages = ""
        for lang in skill_data['languages']:
            languages += f'<p>{lang}</p>'
        lang_block = f'''
            <div class="subheading mb-3">Languages</div><ul>
                {languages}
            </ul>
        '''
        highlights = ""
        for hl in skill_data['highlights']:
            highlights += f'<p>{hl}</p>'
        hl_block = f'''
            <div class="subheading mb-3">Highlights</div>
                <ul>
                    {highlights}
                </ul>
        '''
        return f'''
            <!-- Skills-->
            <section class="resume-section" id="skills">
                <div class="resume-section-content">
                    <h2 class="mb-5">Skills</h2>
                        <div class="subheading mb-3">Technologies & Tools</div>
                            {icons_block}
                            {lang_block}
                            {hl_block}
                </div>
            </section>
            <hr class="m-0" />
        '''
    def certifications(self):
        certifications = ""
        for cert in self.siteData['resumeData']['certifications']:
            certifications += f'''
                <li>
                    <a href="{cert['credentialUrl']}">{cert['title']}</a><br>
                    {cert['dateEarned']} - {cert['dateExpires']}<br><br>
                </li>
            '''
        return f'''
            <!-- Certifications-->
            <section class="resume-section" id="certifications">
                <div class="resume-section-content">
                    <h2 class="mb-5">Certifications</h2>
                    <ul class="fa-ul mb-0">
                        {certifications}
                    </ul>
                </div>
            </section>
        '''
    def resume_section(self):
        return self.about() + self.experience() + self.education() + self.skills() + self.certifications()
    def resume_page(self):
        return f'''
            <iframe frameborder="0" scrolling="no" src="{self.siteData['siteConfig']['embedResume']}" style="width: 75%; height: 1500px"></iframe>
        '''

site_data = os.getcwd() + '/public/siteData.json'

def render_index():
    builder = static_html_builder(site_data=site_data, page='index.html')
    render_content = {}
    render_content['resume'] = builder.resume()
    render_content['profile'] = builder.profile()
    render_content['renderedContent'] = builder.resume_section()
    render_content['siteTitle'] = builder.siteData['siteConfig']['title']
    builder.build(render_content)

def render_resume():
    builder = static_html_builder(site_data=site_data, page='resume.html')
    render_content = {}
    render_content['profile'] = builder.profile()
    render_content['siteTitle'] = builder.siteData['siteConfig']['title']
    render_content['resumeIframe'] = builder.resume_page()
    builder.build(render_content)

if __name__ == "__main__":
    render_index()
    render_resume()