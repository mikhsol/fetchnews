import hashlib

TG_BASE_URL = "https://www.theguardian.com/au"
TG_LINKS = ['https://www.theguardian.com/us-news/2017/aug/23/donald-trump-arizona-rally-phoenix',
            'https://www.theguardian.com/us-news/2017/aug/23/joe-arpaio-donald-trump-signals-presidential-pardon-for'
            '-controversial-sheriff', 'https://www.theguardian.com/us-news/2017/aug/23/joe-arpaio-donald-trump'
                                      '-signals-presidential-pardon-for-controversial-sheriff',
            'https://www.theguardian.com/us-news/2017/aug/23/donald-trump-arizona-rally-phoenix',
            'https://www.theguardian.com/australia-news/2017/aug/23/aboriginal-leader-withdraws-support-for-cashless'
            '-welfare-card-and-says-he-feels-used',
            'https://www.theguardian.com/australia-news/2017/aug/23/aboriginal-leader-withdraws-support-for-cashless'
            '-welfare-card-and-says-he-feels-used',
            'https://www.theguardian.com/australia-news/2017/aug/23/schoolboy-17-lodges-discrimination-complaint-over'
            '-same-sex-marriage-survey', 'https://www.theguardian.com/australia-news/2017/aug/23/schoolboy-17-lodges'
                                         '-discrimination-complaint-over-same-sex-marriage-survey',
            'https://www.theguardian.com/australia-news/2017/aug/23/nsw-minister-furious-after-hsc-students-taught'
            '-incorrect-maths-course', 'https://www.theguardian.com/australia-news/2017/aug/23/nsw-minister-furious'
                                       '-after-hsc-students-taught-incorrect-maths-course',
            'https://www.theguardian.com/australia-news/2017/aug/23/citizenship-changes-are-risky-says-australian'
            '-human-rights-commission', 'https://www.theguardian.com/australia-news/2017/aug/23/citizenship-changes'
                                        '-are-risky-says-australian-human-rights-commission',
            'https://www.theguardian.com/world/2017/aug/23/danish-police-confirm-torso-found-copenhagen-journalist'
            '-kim-wall', 'https://www.theguardian.com/world/2017/aug/23/danish-police-confirm-torso-found-copenhagen'
                         '-journalist-kim-wall',
            'https://www.theguardian.com/australia-news/2017/aug/23/sydney-under-pressure-over-captain-cook-statue'
            '-claim-he-discovered-australia',
            'https://www.theguardian.com/australia-news/2017/aug/23/sydney-under-pressure-over-captain-cook-statue'
            '-claim-he-discovered-australia',
            'https://www.theguardian.com/australia-news/2017/aug/23/victoria-moves-to-become-first-state-to-enshrine'
            '-renewable-energy-targets-in-law',
            'https://www.theguardian.com/australia-news/2017/aug/23/victoria-moves-to-become-first-state-to-enshrine'
            '-renewable-energy-targets-in-law',
            'https://www.theguardian.com/australia-news/2017/aug/23/nsw-opposition-calls-for-public-holiday-honouring'
            '-indigenous-australians', 'https://www.theguardian.com/australia-news/2017/aug/23/nsw-opposition-calls'
                                       '-for-public-holiday-honouring-indigenous-australians',
            'https://www.theguardian.com/australia-news/2017/aug/23/pregnancy-and-mental-health-should-be-covered-by'
            '-all-private-insurance-say-doctors',
            'https://www.theguardian.com/australia-news/2017/aug/23/pregnancy-and-mental-health-should-be-covered-by'
            '-all-private-insurance-say-doctors',
            'https://www.theguardian.com/commentisfree/2017/aug/23/the-alp-policy-on-reproductive-rights-for-women-on'
            '-nauru-silence', 'https://www.theguardian.com/commentisfree/2017/aug/23/the-alp-policy-on-reproductive'
                              '-rights-for-women-on-nauru-silence',
            'https://www.theguardian.com/music/2017/aug/23/klf-bill-drummond-jimmy-cauty-2023-book',
            'https://www.theguardian.com/music/2017/aug/23/klf-bill-drummond-jimmy-cauty-2023-book',
            'https://www.theguardian.com/books/gallery/2017/aug/23/x-rated-film-posters-60s-70s-in-pictures',
            'https://www.theguardian.com/books/gallery/2017/aug/23/x-rated-film-posters-60s-70s-in-pictures',
            'https://www.theguardian.com/commentisfree/2017/aug/23/racial-tensions-are-at-a-high-are-we-on-the-verge'
            '-of-another-cronulla', 'https://www.theguardian.com/commentisfree/2017/aug/23/racial-tensions-are-at-a'
                                    '-high-are-we-on-the-verge-of-another-cronulla',
            'https://www.theguardian.com/world/2017/aug/23/silicon-valley-big-data-extraction-amazon-whole-foods'
            '-facebook', 'https://www.theguardian.com/world/2017/aug/23/silicon-valley-big-data-extraction-amazon'
                         '-whole-foods-facebook',
            'https://www.theguardian.com/commentisfree/2017/aug/23/as-faith-leaders-we-asked-frydenberg-to-cancel-the'
            '-adani-mine-its-a-simple-moral-choice',
            'https://www.theguardian.com/commentisfree/2017/aug/23/as-faith-leaders-we-asked-frydenberg-to-cancel-the'
            '-adani-mine-its-a-simple-moral-choice',
            'https://www.theguardian.com/australia-news/2017/aug/23/the-answers-in-the-post-australian-marriage'
            '-equality-vote-explainer', 'https://www.theguardian.com/australia-news/2017/aug/23/the-answers-in-the'
                                        '-post-australian-marriage-equality-vote-explainer',
            'https://www.theguardian.com/world/2017/aug/23/hey-macarena-saudi-police-detain-14-year-old-boy-for'
            '-dancing-in-the-street', 'https://www.theguardian.com/world/2017/aug/23/hey-macarena-saudi-police-detain'
                                      '-14-year-old-boy-for-dancing-in-the-street',
            'https://www.theguardian.com/sport/2017/aug/23/fifa-puts-pressure-on-ffa-to-find-end-to-crisis-before'
            '-november-deadline', 'https://www.theguardian.com/football/2017/aug/22/barcelona-sue-neymar-world-record'
                                  '-psg-transfer',
            'https://www.theguardian.com/football/2017/aug/22/barcelona-sue-neymar-world-record-psg-transfer',
            'https://www.theguardian.com/sport/2017/aug/23/fifa-puts-pressure-on-ffa-to-find-end-to-crisis-before'
            '-november-deadline', 'https://www.theguardian.com/sport/2017/aug/23/boxing-hype-connor-mcgregor-fight'
                                  '-against-floyd-mayweather-set-to-break-viewing-records',
            'https://www.theguardian.com/sport/2017/aug/22/inside-conor-mcgregor-dublin-making-fighting-superstar'
            '-floyd-mayweather', 'https://www.theguardian.com/sport/2017/aug/22/inside-conor-mcgregor-dublin-making'
                                 '-fighting-superstar-floyd-mayweather',
            'https://www.theguardian.com/sport/2017/aug/23/boxing-hype-connor-mcgregor-fight-against-floyd-mayweather'
            '-set-to-break-viewing-records',
            'https://www.theguardian.com/sport/2017/aug/23/western-force-win-right-to-appeal-hearing-over-super-rugby'
            '-axing', 'https://www.theguardian.com/sport/2017/aug/22/western-force-to-consider-new-asian-competition'
                      '-if-super-rugby-appeal-fails',
            'https://www.theguardian.com/sport/2017/aug/22/western-force-to-consider-new-asian-competition-if-super'
            '-rugby-appeal-fails', 'https://www.theguardian.com/sport/2017/aug/23/western-force-win-right-to-appeal'
                                   '-hearing-over-super-rugby-axing',
            'https://www.theguardian.com/sport/2017/aug/23/cricket-australia-to-resell-nearly-3000-scalped-ashes'
            '-tickets', 'https://www.theguardian.com/sport/2017/aug/22/geoffrey-boycott-apology-unacceptable-remark'
                        '-west-indies', 'https://www.theguardian.com/sport/2017/aug/22/geoffrey-boycott-apology'
                                        '-unacceptable-remark-west-indies',
            'https://www.theguardian.com/sport/2017/aug/23/cricket-australia-to-resell-nearly-3000-scalped-ashes'
            '-tickets', 'https://www.theguardian.com/football/2017/aug/23/socceroos-captain-mile-jedinak-ruled-out-of'
                        '-crucial-world-cup-qualifiers',
            'https://www.theguardian.com/football/2017/aug/23/socceroos-captain-mile-jedinak-ruled-out-of-crucial'
            '-world-cup-qualifiers', 'https://www.theguardian.com/football/2017/aug/22/fancy-bears-accuse-25-players'
                                     '-of-being-given-tues-during-2010-world-cup',
            'https://www.theguardian.com/football/2017/aug/22/fancy-bears-accuse-25-players-of-being-given-tues'
            '-during-2010-world-cup', 'https://www.theguardian.com/sport/2017/aug/22/geelong-could-miss-out-on-home'
                                      '-afl-final-with-mcg-potentially-vacant',
            'https://www.theguardian.com/sport/2017/aug/22/geelong-could-miss-out-on-home-afl-final-with-mcg'
            '-potentially-vacant', 'https://www.theguardian.com/commentisfree/2017/aug/23/diana-death-britain-stiff'
                                   '-upper-lip',
            'https://www.theguardian.com/commentisfree/2017/aug/23/diana-death-britain-stiff-upper-lip',
            'https://www.theguardian.com/commentisfree/2017/aug/23/turnbulls-counter-terrorism-plan-goes-beyond'
            '-whether-our-cities-needs-bollards-or-not',
            'https://www.theguardian.com/commentisfree/2017/aug/23/turnbulls-counter-terrorism-plan-goes-beyond'
            '-whether-our-cities-needs-bollards-or-not',
            'https://www.theguardian.com/commentisfree/2017/aug/22/trump-mar-a-lago-travel-secret-service-cost',
            'https://www.theguardian.com/commentisfree/2017/aug/22/trump-mar-a-lago-travel-secret-service-cost',
            'https://www.theguardian.com/commentisfree/2017/aug/22/bra-checks-football-fans-criminals-stevenage-fc',
            'https://www.theguardian.com/commentisfree/2017/aug/22/bra-checks-football-fans-criminals-stevenage-fc',
            'https://www.theguardian.com/commentisfree/2017/aug/22/the-guardian-view-on-trump-and-afghanistan'
            '-unwinnable-and-unlosable', 'https://www.theguardian.com/commentisfree/2017/aug/22/the-guardian-view-on'
                                         '-trump-and-afghanistan-unwinnable-and-unlosable',
            'https://www.theguardian.com/commentisfree/2017/aug/22/positive-trump-media-coverage-when-he-embraces-war'
            '', 'https://www.theguardian.com/commentisfree/2017/aug/22/positive-trump-media-coverage-when-he-embraces'
                '-war', 'https://www.theguardian.com/us-news/gallery/2017/aug/23/protests-at-donald-trump-rally-in'
                        '-phoenix-in-pictures',
            'https://www.theguardian.com/us-news/gallery/2017/aug/23/protests-at-donald-trump-rally-in-phoenix-in'
            '-pictures', 'https://www.theguardian.com/uk-news/video/2017/aug/23/harry-and-william-talk-about-impact'
                         '-of-losing-diana-video',
            'https://www.theguardian.com/uk-news/video/2017/aug/23/harry-and-william-talk-about-impact-of-losing'
            '-diana-video', 'https://www.theguardian.com/world/video/2017/aug/23/high-waves-crash-on-coastline-as'
                            '-typhoon-hato-hits-hong-kong-video',
            'https://www.theguardian.com/world/video/2017/aug/23/high-waves-crash-on-coastline-as-typhoon-hato-hits'
            '-hong-kong-video', 'https://www.theguardian.com/us-news/video/2017/aug/23/trump-lashes-out-at-truly'
                                '-dishonest-media-reporting-of-charlottesville-video',
            'https://www.theguardian.com/us-news/video/2017/aug/23/trump-lashes-out-at-truly-dishonest-media'
            '-reporting-of-charlottesville-video',
            'https://www.theguardian.com/uk-news/video/2017/aug/22/driver-walks-away-with-bruises-after-250mph-crash'
            '-video', 'https://www.theguardian.com/uk-news/video/2017/aug/22/driver-walks-away-with-bruises-after'
                      '-250mph-crash-video',
            'https://www.theguardian.com/stage/video/2017/aug/22/edinburgh-fringe-ken-cheng-funniest-jokes-from-2012'
            '-to-2017-video', 'https://www.theguardian.com/stage/video/2017/aug/22/edinburgh-fringe-ken-cheng'
                              '-funniest-jokes-from-2012-to-2017-video',
            'https://www.theguardian.com/news/gallery/2017/aug/22/some-nosey-opera-singers-and-dancing-robots-todays'
            '-unmissable-photos', 'https://www.theguardian.com/news/gallery/2017/aug/22/some-nosey-opera-singers-and'
                                  '-dancing-robots-todays-unmissable-photos',
            'https://www.theguardian.com/world/2017/aug/23/refugees-needing-high-level-treatment-should-be-brought-to'
            '-australia-medical-bodies-say',
            'https://www.theguardian.com/world/2017/aug/23/refugees-needing-high-level-treatment-should-be-brought-to'
            '-australia-medical-bodies-say',
            'https://www.theguardian.com/australia-news/2017/aug/23/commonwealth-bank-faces-class-action-over-money'
            '-laundering-allegations', 'https://www.theguardian.com/australia-news/2017/aug/23/commonwealth-bank'
                                       '-faces-class-action-over-money-laundering-allegations',
            'https://www.theguardian.com/australia-news/2017/aug/23/norfolk-island-should-become-part-of-new-zealand'
            '-says-former-chief-minister',
            'https://www.theguardian.com/australia-news/2017/aug/23/norfolk-island-should-become-part-of-new-zealand'
            '-says-former-chief-minister',
            'https://www.theguardian.com/australia-news/2017/aug/23/australia-refuses-to-rule-out-sending-more-troops'
            '-to-afghanistan-under-trump-surge',
            'https://www.theguardian.com/australia-news/2017/aug/23/australia-refuses-to-rule-out-sending-more-troops'
            '-to-afghanistan-under-trump-surge',
            'https://www.theguardian.com/australia-news/2017/aug/23/mayor-kept-in-dark-about-drug-tests-trial-for'
            '-welfare-recipients-in-logan-city',
            'https://www.theguardian.com/australia-news/2017/aug/23/mayor-kept-in-dark-about-drug-tests-trial-for'
            '-welfare-recipients-in-logan-city',
            'https://www.theguardian.com/australia-news/2017/aug/23/arena-to-provide-12m-for-new-battery-at-dalrymple'
            '-electricity-substation', 'https://www.theguardian.com/australia-news/2017/aug/23/arena-to-provide-12m'
                                       '-for-new-battery-at-dalrymple-electricity-substation',
            'https://www.theguardian.com/australia-news/2017/aug/23/arms-manufacturers-allowed-to-bypass'
            '-discrimination-laws-in-nsw',
            'https://www.theguardian.com/australia-news/2017/aug/23/arms-manufacturers-allowed-to-bypass'
            '-discrimination-laws-in-nsw',
            'https://www.theguardian.com/australia-news/2017/aug/23/industrial-manslaughter-laws-to-be-brought-in'
            '-after-dreamworld-deaths',
            'https://www.theguardian.com/australia-news/2017/aug/23/industrial-manslaughter-laws-to-be-brought-in'
            '-after-dreamworld-deaths', 'https://www.theguardian.com/world/2017/aug/23/please-stop-brutal-killing-of'
                                        '-a-student-in-philippines-drug-war-sparks-nationwide-anger',
            'https://www.theguardian.com/world/2017/aug/23/please-stop-brutal-killing-of-a-student-in-philippines'
            '-drug-war-sparks-nationwide-anger',
            'https://www.theguardian.com/us-news/2017/aug/23/trump-russia-dossier-owner-faces-senators-donald-jr'
            '-still-a-no-show', 'https://www.theguardian.com/us-news/2017/aug/23/trump-russia-dossier-owner-faces'
                                '-senators-donald-jr-still-a-no-show',
            'https://www.theguardian.com/global-development/2017/aug/23/indian-woman-granted-divorce-over-lack-of'
            '-toilet-sanitation-every-day-was-agony',
            'https://www.theguardian.com/global-development/2017/aug/23/indian-woman-granted-divorce-over-lack-of'
            '-toilet-sanitation-every-day-was-agony',
            'https://www.theguardian.com/world/2017/aug/23/tony-de-brum-champion-of-paris-climate-agreement-dies-aged'
            '-72', 'https://www.theguardian.com/world/2017/aug/23/tony-de-brum-champion-of-paris-climate-agreement'
                   '-dies-aged-72', 'https://www.theguardian.com/world/2017/aug/23/bbc-journalist-jonathan-head-on'
                                    '-trial-in-thailand-over-unusual-defamation-case',
            'https://www.theguardian.com/world/2017/aug/23/bbc-journalist-jonathan-head-on-trial-in-thailand-over'
            '-unusual-defamation-case', 'https://www.theguardian.com/world/2017/aug/23/north-koreans-fear-more'
                                        '-sanctions-as-drought-pushes-millions-towards-malnutrition',
            'https://www.theguardian.com/world/2017/aug/23/north-koreans-fear-more-sanctions-as-drought-pushes'
            '-millions-towards-malnutrition',
            'https://www.theguardian.com/world/2017/aug/23/typhoon-hato-hong-kong-battens-down-as-storm-closes'
            '-schools-and-stock-market',
            'https://www.theguardian.com/world/2017/aug/23/typhoon-hato-hong-kong-battens-down-as-storm-closes'
            '-schools-and-stock-market', 'https://www.theguardian.com/world/2017/aug/22/spain-terror-suspect-mohamed'
                                         '-houli-tells-court-cell-planning-bigger-attack',
            'https://www.theguardian.com/world/2017/aug/22/spain-terror-suspect-mohamed-houli-tells-court-cell'
            '-planning-bigger-attack', 'https://www.theguardian.com/cities/2017/aug/23/america-alt-weeklies-baltimore'
                                       '-city-paper-village-voice',
            'https://www.theguardian.com/cities/2017/aug/23/america-alt-weeklies-baltimore-city-paper-village-voice',
            'https://www.theguardian.com/culture/2017/aug/22/museum-visitors-photo-stunt-damages-800-year-old-coffin'
            '-essex', 'https://www.theguardian.com/culture/2017/aug/22/museum-visitors-photo-stunt-damages-800-year'
                      '-old-coffin-essex',
            'https://www.theguardian.com/technology/2017/aug/23/dark-web-neo-nazis-tor-dissidents-white-supremacists'
            '-criminals-paedophile-rings',
            'https://www.theguardian.com/technology/2017/aug/23/dark-web-neo-nazis-tor-dissidents-white-supremacists'
            '-criminals-paedophile-rings',
            'https://www.theguardian.com/film/2017/aug/23/martin-scorsese-to-produce-gritty-and-grounded-joker-origin'
            '-story-reports', 'https://www.theguardian.com/film/2017/aug/23/martin-scorsese-to-produce-gritty-and'
                              '-grounded-joker-origin-story-reports',
            'https://www.theguardian.com/world/2017/aug/23/we-would-rather-die-than-stay-there-the-refugees-crossing'
            '-from-morocco-to-spain', 'https://www.theguardian.com/world/2017/aug/23/we-would-rather-die-than-stay'
                                      '-there-the-refugees-crossing-from-morocco-to-spain',
            'https://www.theguardian.com/small-business-network/2017/aug/23/side-business-career-advice-freedom-to'
            '-exist', 'https://www.theguardian.com/small-business-network/2017/aug/23/side-business-career-advice'
                      '-freedom-to-exist',
            'https://www.theguardian.com/travel/2017/aug/23/cycling-break-norway-senja-island-fjords',
            'https://www.theguardian.com/travel/2017/aug/23/cycling-break-norway-senja-island-fjords',
            'https://www.theguardian.com/science/audio/2017/aug/23/being-human-in-the-age-of-artificial-intelligence'
            '-science-weekly-podcast', 'https://www.theguardian.com/science/audio/2017/aug/23/being-human-in-the-age'
                                       '-of-artificial-intelligence-science-weekly-podcast',
            'https://www.theguardian.com/culture/2017/aug/22/hate-groups-in-pop-culture-failure-neo-nazis',
            'https://www.theguardian.com/culture/2017/aug/22/hate-groups-in-pop-culture-failure-neo-nazis',
            'https://www.theguardian.com/music/2017/aug/23/morrissey-new-record-will-capture-the-zeitgeist-of-an-ever'
            '-changing-world', 'https://www.theguardian.com/music/2017/aug/23/morrissey-new-record-will-capture-the'
                               '-zeitgeist-of-an-ever-changing-world',
            'https://www.theguardian.com/film/2017/aug/22/gemma-arterton-studio-forced-her-to-lose-weight-morocco'
            '-film', 'https://www.theguardian.com/film/2017/aug/22/gemma-arterton-studio-forced-her-to-lose-weight'
                     '-morocco-film', 'https://www.theguardian.com/media/shortcuts/2017/aug/22/louise-linton-wife'
                                      '-steven-mnuchin-self-sacfricice-instagram',
            'https://www.theguardian.com/media/shortcuts/2017/aug/22/louise-linton-wife-steven-mnuchin-self'
            '-sacfricice-instagram', 'https://www.theguardian.com/uk-news/2017/aug/23/prince-william-queen-shielded'
                                     '-us-from-public-grief-after-dianas-death',
            'https://www.theguardian.com/uk-news/2017/aug/23/prince-william-queen-shielded-us-from-public-grief-after'
            '-dianas-death', 'https://www.theguardian.com/artanddesign/gallery/2017/aug/23/rene-magritte-130-photos'
                             '-featured-in-world-first-exhibition-in-pictures',
            'https://www.theguardian.com/artanddesign/gallery/2017/aug/23/rene-magritte-130-photos-featured-in-world'
            '-first-exhibition-in-pictures',
            'https://www.theguardian.com/books/gallery/2017/aug/23/x-rated-film-posters-60s-70s-in-pictures',
            'https://www.theguardian.com/us-news/2017/aug/23/donald-trump-arizona-rally-phoenix',
            'https://www.theguardian.com/world/2017/aug/23/danish-police-confirm-torso-found-copenhagen-journalist'
            '-kim-wall', 'https://www.theguardian.com/commentisfree/2017/aug/23/the-alp-policy-on-reproductive-rights'
                         '-for-women-on-nauru-silence',
            'https://www.theguardian.com/australia-news/2017/aug/23/aboriginal-leader-withdraws-support-for-cashless'
            '-welfare-card-and-says-he-feels-used',
            'https://www.theguardian.com/australia-news/2017/aug/23/nsw-minister-furious-after-hsc-students-taught'
            '-incorrect-maths-course', 'https://www.theguardian.com/australia-news/2017/aug/23/schoolboy-17-lodges'
                                       '-discrimination-complaint-over-same-sex-marriage-survey',
            'https://www.theguardian.com/uk-news/2017/aug/23/prince-william-queen-shielded-us-from-public-grief-after'
            '-dianas-death', 'https://www.theguardian.com/global-development/2017/aug/23/indian-woman-granted-divorce'
                             '-over-lack-of-toilet-sanitation-every-day-was-agony',
            'https://www.theguardian.com/australia-news/2017/aug/23/sydney-under-pressure-over-captain-cook-statue'
            '-claim-he-discovered-australia']
TG_ARTICLE_URL = 'https://www.theguardian.com/australia-news/2017/aug/20/george-brandis-says-citizenship-crisis-will' \
                 '-last-for-months-as-labor-attacks-circus '
TG_AUTHORS = ["Calla Wahlquist", "Gareth Hutchens"]
TG_HEADLINE = "Coalition says citizenship crisis will last months but MPs " \
           "will keep voting"
TG_DATE = "Sunday 20 August 2017 05.34 BST"
TG_TEXT = "The Turnbull government says if any more Coalition MPs are found to be dual citizens they will continue to " \
       "vote in parliament until the high court settles their eligibility.Arthur Sinodinos, the minister for " \
       "industry, innovation and science, has said it was wrong for theNationals senator Matt Canavan to promise to " \
       "refrain from voting in parliamentafter he discovered he held dual Italian citizenship, because he did so when " \
       "he did not know all the details of his case.He said the Nationals leader, Barnaby Joyce, and the deputy " \
       "Nationals leader, Fiona Nash –who have also discovered they are dual citizens– were right to keep voting in " \
       "parliament until their eligibility was settled by the high court.He said Joyce and Nash would be the standard " \
       "for any other Turnbull government MPs who may be found to be dual citizens.“I think the standard that’s been " \
       "set will now stick,” Sinodinos told the ABC on Sunday. “What we need to do is make sure everybody takes " \
       "responsibility for their own situation, in terms of members of parliament, and we work our way through this " \
       "as quickly as possible, get the high court to make decisions relevant to what’s going on and we move on.”The " \
       "decision to keep all Coalition MPs voting in parliament is an attempt by the Turnbull government to retain " \
       "control of the House of Representatives, where it holds a one-seat majority.The attorney general, " \
       "George Brandis, believes the high court won’t be dealing withthe citizenship crisis that has embroiled seven " \
       "MPs and senatorsuntil October, leaving that majority in the balance.If Joyce is found by the court to be " \
       "ineligible to sit in the parliament, it would trigger a byelection in his seat of New England.Brandis said " \
       "the legal advice he had received said there was no problem with Joyce and Nash remaining in the cabinet and " \
       "making executive decisions.“If there is anyone who is a threat to the integrity of the parliament at the " \
       "moment is [opposition leader Bill] Shorten because of the devious tactics he has employed,” he said.Shorten, " \
       "whose father was born in the UK, said on Sunday that he renounced his British citizenship “many years ago” " \
       "but would not provide documentary evidence, telling reporters: “I don’t feel any obligation to justify what I " \
       "have just said because I know it to be true ... I don’t expect every MP to have to jump through hoops to " \
       "start meeting a standard that we have already met.”Shorten said all candidates for federal parliament should " \
       "be aware of the citizenship requirements and criticised the government for turning a legal issue into a " \
       "“parliamentary farce”.“The advice about section 44 is on the candidates’ form when people nominate so it’s a " \
       "matter of just reading the fine print,” he said. “Perhaps this is a problem in terms of the constitution that " \
       "has been ignored but it is still the constitution of Australia and, until the constitution is changed, " \
       "it’s the law.”Shorten did, however, say he was willing to offer the federal government a “peace treaty” over " \
       "the citizenship crisis. The Labor leader said Joyce and Nash should stand aside until the high court decides " \
       "their fate but was willing to discuss the matter with the prime minister. However, he suggested that, " \
       "if there was a controversial vote to be had in parliament, it should wait until the high court has made its " \
       "decision.“I think Australians want to see this government focusing on them, not these legal and political " \
       "games,” Shorten said.Sinodinos dismissed concerns that the validity of Turnbull government decisions could be " \
       "challenged in court if Coalition MPs were proven to have been ineligible.“The advice I have received to date " \
       "is that decisions in the parliament and decisions by ministers, the validity of those decisions, will not be " \
       "affected,” he said.ABC host Chris Ulhmann then asked: “If it turns out that Barnaby Joyce should not have " \
       "been in cabinet … people can take it to court, and we’ve seen plenty of ‘lawfare’, particularly from " \
       "environmental groups, they may well decide to test that argument in another court?”Sinodinos replied: “I’m " \
       "not going to speculate on where the high court will come out. The point is that there was very strong advice " \
       "given to the government about whether Mr Joyce stands [and] Fiona Nash.”On Saturday, the crossbench " \
       "senatorNick Xenophonsaid he would become the seventh MP to refer himself to the high court after he " \
       "discovered he was a British overseas citizen.He said he had received advice from the British Home Office that " \
       "it considered him a British overseas citizenbecause his father, Theodoros Xenophou , was from Cyprus – a " \
       "British colony until 1960 – and moved to Australia in 1951.When Cyprus gained independence, most Cypriots " \
       "lost their British citizenship except those who moved to one of nine countries, including Australia. This " \
       "made Xenophon’s father a British overseas citizen, a status that automatically extended to Xenophon, " \
       "who was born in Australia.“The legal advice I have had is that I should just keep calm and carry on and wait " \
       "for the high court to determine this,” he told the Nine network on Sunday.On Sunday Shorten denied " \
       "allegations Labor staffers had been involved in uncovering details of Xenophon’s UK citizenship.“I rang " \
       "senator Xenophon last night,” he said. “I understand that he’s upset at what would seem to be clearly quite " \
       "an anachronism, a colonial loophole that he’s caught in... But I made it clear to him that whilst he may have " \
       "made some intemperate remarks, and I understand he would be upset about being in this predicament, " \
       "Labor had nothing to do with it. Full stop.”The parliament has already referred Canavan, the Greens senators " \
       "Larissa Waters and Scott Ludlam, and the One Nation senator Malcolm Roberts,as well as Joyce, to the court. " \
       "On Friday night, Nash revealed she was a UK citizen by descent – the third member of the prime minister’s " \
       "cabinet to be affected.The senior Nationals MP Darren Chester conceded it had been a “rotten few weeks” for " \
       "his party. “We need to be better at our vetting process when people nominate to be a candidate,” he told ABC " \
       "television.The high court will have a directions hearing on the matter on Thursday where a judge will get the " \
       "parties together and agree to a timetable over the various steps towards the hearings.“The commonwealth will " \
       "be asking the court to deal with the matter urgently,” Brandis told Sky News. While the court will have a " \
       "sitting in September, he thinks realistically the issue won’t be heard until the first fortnight of " \
       "October.The shadow attorney general, Mark Dreyfus, said the high court had a record of dealing very quickly " \
       "with urgent cases and hoped it will be cleared up within a couple of months.“I think every Australian will be " \
       "looking at this and thinking what a circus,” he told ABC television.Xenophon said Joyce’s decision not to " \
       "stand down was causing disruption on the floor of the House of Representatives.“It would probably be simpler " \
       "for the government if the ministers stood aside but it’s really a political issue, not a legal issue," \
       "” he later told Sky News.At the conclusion of the last federal election, the government entered agreements " \
       "for confidence and supply with some of the lower house crossbenchers as a precautionary measure, " \
       "but last week independent MP Bob Katter said he would no longer guarantee supply and confidence to the " \
       "government.Xenophon confirmed his NXT party would still support the government on matters of confidence and " \
       "supply.Australian Associated Press contributed to this report ".strip()
TG_ID = hashlib.sha3_256(bytes(TG_ARTICLE_URL + TG_DATE, 'utf-16be')).hexdigest()
