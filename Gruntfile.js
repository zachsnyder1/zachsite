module.exports = function(grunt) {
	// Configuration
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		jshint: {
			options: {
				force: true,
			},
			src: [ 
				'./{zachsite,projects,blog,geopost}/static/**/*.js',
				'./{zachsite,projects,blog,geopost}/qunit_tests/*.js',
				'!./zachsite/static/zachsite/bootstrap.js',
				'!./geopost/static/geopost/ol.js',
				'!./geopost/static/geopost/uuid.js'
			]
		},
		sass: {
			zachsite: {
				files: {
					'./zachsite/static/zachsite/index.css': './style_prep/index.scss',
					'./zachsite/static/zachsite/404.css': './style_prep/404.scss'
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
			},
			geopost: {
				files: {
					'./geopost/static/geopost/entry.css': './style_prep/geopost_entry.scss',
					'./geopost/static/geopost/home_anonymous.css': './style_prep/geopost_home_anonymous.scss',
					'./geopost/static/geopost/home_authenticated.css': './style_prep/geopost_home_authenticated.scss'
				}
			}
		},
		concat: {
			zachsite: {
				files: {
					'./zachsite/static/zachsite/index_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./zachsite/static/zachsite/index.js'
					],
				},
			},
			projects: {
				files: {
					'./projects/static/projects/projects_home_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./projects/static/projects/projects_base.js', 
						'./projects/static/projects/projects_home.js'
					],
					'./projects/static/projects/project_about_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./projects/static/projects/projects_base.js', 
						'./projects/static/projects/project_about.js'
					],
					'./projects/static/projects/project_docs_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./projects/static/projects/projects_base.js', 
						'./projects/static/projects/project_docs.js'
					]
				},
			},
			blog: {
				files: {
					'./blog/static/blog/blog_entries_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./blog/static/blog/blog_base.js', 
						'./blog/static/blog/blog_entries.js'
					],
					'./blog/static/blog/blog_detail_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./blog/static/blog/blog_base.js', 
						'./blog/static/blog/blog_detail.js'
					]
				},
			},
			geopost: {
				files: {
					'./geopost/static/geopost/home_anonymous_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./projects/static/projects/projects_base.js', 
						'./geopost/static/geopost/geopost_base.js', 
						'./geopost/static/geopost/home_anonymous.js'
					],
					'./geopost/static/geopost/home_authenticated_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./projects/static/projects/projects_base.js', 
						'./geopost/static/geopost/geopost_base.js', 
						'./geopost/static/geopost/home_authenticated.js'
					],
					'./geopost/static/geopost/entry_concat.js': [
						'./zachsite/static/zachsite/base.js', 
						'./projects/static/projects/projects_base.js', 
						'./geopost/static/geopost/geopost_base.js', 
						'./geopost/static/geopost/entry.js'
					]
				}
			}
		},
		cssmin: {
			zachsite: {
				files: [{
      				expand: true,
      				cwd: './zachsite/static/zachsite/',
      				src: ['*.css', '!*.min.css'],
      				dest: './zachsite/static/zachsite/',
      				ext: '.min.css'
    			}]
			},
			projects: {
				files: [{
      				expand: true,
      				cwd: './projects/static/projects/',
      				src: ['*.css', '!*.min.css'],
      				dest: './projects/static/projects/',
      				ext: '.min.css'
    			}]
			},
			blog: {
				files: [{
      				expand: true,
      				cwd: './blog/static/blog/',
      				src: ['*.css', '!*.min.css'],
      				dest: './blog/static/blog/',
      				ext: '.min.css'
    			}]
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
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-cssmin');
	grunt.loadNpmTasks('grunt-contrib-qunit');
	// register tasks
	grunt.registerTask(
		'default', 
		['concat', 'jshint', 'sass', 'cssmin', 'clean:sass_map', 'qunit']
	);
};
