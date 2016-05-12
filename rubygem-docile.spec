%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name docile

Summary:       Docile keeps your Ruby DSLs tame and well-behaved
Name:          %{?scl_prefix}rubygem-%{gem_name}
Version:       1.1.5
Release:       4%{?dist}
Group:         Development/Languages
License:       MIT
URL:           https://ms-ati.github.com/docile/
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix}rubygem(mime-types)
BuildRequires: %{?scl_prefix}rubygem(rspec)
# coveralls is now optional for tests
# Add back when coveralls is in Fedora
#BuildRequires: %{?scl_prefix}rubygem(coveralls)
# Dependencies are missing
#  - test suite passes
#  - avoids unnecessary dependencies in SCL
#BuildRequires: %{?scl_prefix}rubygem(redcarpet)
#BuildRequires: %{?scl_prefix}rubygem(yard)
#BuildRequires: %{?scl_prefix}rubygem(rake)
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Docile turns any Ruby object into a DSL.
Especially useful with the Builder pattern.

%package doc
Summary:   Documentation for %{pkg_name}
Group:     Documentation
Requires:  %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

# Remove build leftovers.
rm -rf %{buildroot}%{gem_instdir}/{.coveralls.yml,.gitignore,.rspec,.ruby-gemset,.ruby-version,.travis.yml,.yard*}

%check
%{?scl:scl enable %{scl} - << \EOF}
rspec -Ilib spec
%{?scl:EOF}

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/docile.gemspec
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/on_what.rb
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Wed Apr 06 2016 Pavel Valena <pvalena@redhat.com> - 1.1.5-4
- Add scl macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Troy Dawson <tdawson@redhat.com> - 1.1.5-1
- Updated to latest release

* Fri Jun 13 2014 Troy Dawson <tdawson@redhat.com> - 1.1.4-1
- Update to version 1.1.4
- Tests now run without coveralls

* Wed Apr 02 2014 Troy Dawson <tdawson@redhat.com> - 1.1.3-1
- Initial package
