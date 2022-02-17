import {library, dom,} from '@fortawesome/fontawesome-svg-core';
import {faUser, faCopy, faTimesCircle, faRss, faCalendar, faBookOpen, faLink} from '@fortawesome/free-solid-svg-icons';
import {faGithub, faPython} from '@fortawesome/free-brands-svg-icons';

library.add(
  faUser,
  faGithub,
  faCopy,
  faTimesCircle,
  faPython,
  faRss,
  faCalendar,
  faBookOpen,
  faLink
);
dom.watch();
