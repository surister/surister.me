<template>
  <div class="columns">
    <div class="column is-narrow">
      <div class="content">
        <h1 class="title has-text-white">About me</h1>

        <code-snippet language="Python" version="any" :content="content">
        </code-snippet>

        <p class="subtitle has-text-white pt-5">
          <strong class="has-text-white">This
            is obviously not
            my cv,</strong> <a class="has-text-link">contact</a> me for any further inquiry.
          <br>
        </p>
      </div>
    </div>

  </div>
</template>
<script>

export default {
  components: {  },
  data: function () {
    return {
      'content': `REGION = 'Europe'
LANGUAGES = {'Python', 'JavaScript', 'Dart'}
YEARS_AS_DEVELOPER = ${((new Date() - new Date(2018, 3, 29)) / (1000*60*60*24)) / 365} # Constantly updating
FRAMEWORKS = {'Django', 'Django-drf', 'FastApi', 'Scrappy', 'Vue', 'Nuxtjs' ,'Flutter', 'Buefy'} # To name a few..
JOB_HISTORY = {
    'current_job': {
        'job_title': 'Python Software Engineer',
        'job_description': 'Maintain and improve Big data Pipelines'
    },
    'former_jobs': [
        {
            'job_title': 'Backend Engineer',
            'job_description': 'Build RestFul Api and IOT backends with Django'
        },
        {
            'job_title': 'Full-Stack Engineer',
            'job_description': 'D-O-E-V-E-R-Y-T-H-I-N-G'
        }
    ]
}
HOBBIES = ['Sports', 'Programming', 'OpenSource', 'Video Games', 'Technology']
                `
    }
  }
}
</script>
