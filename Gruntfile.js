module.exports = function(grunt) {
	// Configuration
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		jshint: {
			options: {
				force: true,
			},
			src: [ 
				'./{zachsite,projects,blog}/static/**/*.js',
				'./{zachsite,projects,blog}/qunit_tests/*.js',
				'!./zachsite/static/zachsite/bootstrap.js'
			]
		},
		sass: {
			zachsite: {
				files: {
					'./zachsite/static/zachsite/index.css': './style_prep/index.scss'
				}
			},
			projects: {
				files: {
					'./projects/static/projects/projects_home.css': './style_prep/projects_home.scss',
					'./projects/static/projects/project_about.css': './style_prep/project_about.scss',
					'./projects/static/projects/project_docs.css': './style_prep/project_docs.scss'
				}
			},
			blog: {
				files: {
					'./blog/static/blog/blog_entries.css': './style_prep/blog_entries.scss',
					'./blog/static/blog/blog_detail.css': './style_prep/blog_detail.scss'
				}
			}
		},
		clean: {
			sass_map: ["./{zachsite,projects,blog}/static/**/*.map"],
			pycache: ["./**/__pycache__/**"]
		},
		qunit: {
			all: ['./**/qunit_tests/qunit_*.html']
		}
	});
	
	// load npm modules
	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-jshint');
	grunt.loadNpmTasks('grunt-contrib-clean');
	grunt.loadNpmTasks('grunt-contrib-qunit');
	// register tasks
	grunt.registerTask('default', ['jshint', 'sass', 'clean:sass_map', 'qunit']);
};