module.exports = function(grunt) {

  // configure tasks
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        compass: {
            dist: {
                options: {
                    sassDir: 'sass',
                    cssDir: '../media/paraserry/css',
                    config: 'config.rb'
                }
            }
        },

        concat: {
            options: {
                separator: ';',
            },
            libs: {
                src: [
                    'js/vendor/console-helper.js',
                    'js/vendor/jquery-1.8.3.min.js',
                    'js/vendor/jquery.js',
                    'js/vendor/css_browser_selector.js',
                    'js/vendor/jquery.easing.js',
                    'js/vendor/jquery-ui.min.js',
                    'js/vendor/jquery.html5-placeholder-shim.js',
                    'js/vendor/animatescroll.js',
                    
                ],
                dest: '../media/paraserry/js/paraserry.libs.js',
            },
            core: {
                src: [

                    'js/core.js',
                ],
                dest: '../media/paraserry/js/paraserry.core.js',
            },
            sass: {
                src: [
                    'sass/screen.scss',
                ],
                dest: '../media/paraserry/css/core.css',
            },
        },


        watch: {
            css: {
                files: ['sass/*.scss', 'sass/*/*.scss', 'sass/*/*/*.scss'],
                tasks: ['compass:dist']
            },
            concat: {
                files: ['js/*.js', 'js/*/*.js'],
                tasks: ['concat:libs', 'concat:core', 'concat:sass']
            }
        }
    });

    // load plugins
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-newer');
    grunt.loadNpmTasks('grunt-contrib-concat');

    // register tasks
    grunt.registerTask('default', ['compass:dist','concat:libs', 'concat:core',]);

};