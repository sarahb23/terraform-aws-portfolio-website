document.getElementById('profile').innerHTML = profile();
document.getElementById('about').innerHTML = about();
document.getElementById('education').innerHTML = education();
document.getElementById('experience').innerHTML = experience();
document.getElementById('awards').innerHTML = certifications();
document.getElementById('skills').innerHTML = skills();
// Adds optional Google Analytics tag
if (siteConfig.analyticsId != null) {
    document.getElementsByTagName('head')[0].innerHTML += addAnalytics();
}
// Adds optional navbar link to a PDF resume
if (siteConfig.resumeFileName != null) {
    document.getElementById('resumePDF').innerHTML = `<a class="nav-link" href="docs/${siteConfig.resumeFileName}">PDF Resume</a>`
};
document.getElementsByTagName('title')[0].innerHTML = siteConfig.title;

function profile () {
    let section = `<a class="navbar-brand js-scroll-trigger" href="#page-top">
        <span class="d-block d-lg-none">${resumeData.name[0]} ${resumeData.name[1]}</span>
        <span class="d-none d-lg-block"><img class="img-fluid img-profile rounded-circle mx-auto mb-2" src="${resumeData.profilePicUrl}" alt="" /></span>
    </a>`
    return section;
};

function about () {
    let section = `<div class="resume-section-content">
                    <h1 class="mb-0">
                        ${resumeData.name[0]}
                        <span class="text-primary">${resumeData.name[1]}</span>
                    </h1>
                    <div class="subheading mb-5">
                        <a href="mailto:${resumeData.email}">${resumeData.email}</a>
                    </div>
                    <p class="lead mb-5">${resumeData.aboutMe}</p>
                    <div class="social-icons">
                        <a class="social-icon" href="${resumeData.socialLinks.linkedin.url}"><i class="fab fa-linkedin-in"></i></a>
                        <a class="social-icon" href="${resumeData.socialLinks.github.url}"><i class="fab fa-github"></i></a>
                    </div>
                </div>`
    return section;
};

function addAnalytics () {
    var analyticsId = siteConfig.analyticsId;
    let analytics = `
    <!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=${analyticsId}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '${analyticsId}');
</script>`
    return analytics;
};

function experience () {
    let section = '';
    section += `<div class="resume-section-content">
    <h2 class="mb-5">Experience</h2>`;
    for (x of resumeData.work) {
        section += `
        <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
            <div class="flex-grow-1">
                <h3 class="mb-0">${x.title}</h3>
                <div class="subheading mb-3">${x.companyName}</div>`
                for (i of x.responsibilities) {
                    section += `<p>${i}</p>`
                };
            section += `</div>
                    <div class="flex-shrink-0"><span class="text-primary">${x.dateStarted} - ${x.dateUntil}</span></div>
                </div>`
    };
    section += '</div>';
    return section

};

function education () {
    let section = '';
    section += `<div class="resume-section-content">
    <h2 class="mb-5">Education</h2>`;
    for (x of resumeData.education) {
    section += `<div class="d-flex flex-column flex-md-row justify-content-between mb-5">
        <div class="flex-grow-1">
            <h3 class="mb-0">${x.universityName}</h3>
            <div class="subheading mb-3">${x.degree}</div>
            <div>${x.description}</div>
        </div>
        <div class="flex-shrink-0"><span class="text-primary">${x.dateStarted} - ${x.dateCompleted}</span></div>
    </div>`;
    };
    section += '</div>';
    return section;
};

function certifications () {
    let section = '';
    section += `
    <div class="resume-section-content">
        <h2 class="mb-5">Certifications</h2>
        <ul class="fa-ul mb-0">
    `
    for (x of resumeData.certifications) {
        section += `
        <li>
           <a href="${x.credentialUrl}">${x.title}</a><br>
           ${x.dateEarned} - ${x.dateExpires}<br><br>
        </li>
        `
    };
    section += `
        </ul>
    </div>
    `
    return section;
};

function skills () {
    let section = '';
    section += `<div class="resume-section-content">
    <h2 class="mb-5">Skills</h2>
    <div class="subheading mb-3">Technologies & Tools</div>
    <ul class="list-inline dev-icons">`
    for (x of resumeData.skills.fontAwesomeIcons) {
        section += `<li class="list-inline-item"><i class="fab fa-${x}"></i></li>`
    };
    section += `</ul>
    <div class="subheading mb-3">Languages</div><ul>`
    for (x of resumeData.skills.languages) {
        section += `<p>${x}</p>`
    };
    section += `</ul><div class="subheading mb-3">Highlights</div>
    <ul>`
    for (x of resumeData.skills.highlights) {
        section += `<p>${x}</p>`
    };
    section += `</ul></div>`
    return section;
};