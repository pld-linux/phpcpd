%define		status		stable
%define		pearname	phpcpd
Summary:	Copy/Paste Detector (CPD) for PHP code
Name:		phpcpd
Version:	2.0.0
Release:	4
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	920b308e47ee3e715fe3ed5dbd86f5cd
Patch0:	autoload.patch
URL:		https://github.com/sebastianbergmann/phpcpd
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(tokenizer)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear >= 1.3.14-2
Requires:	php-phpunit-FinderFacade >= 1.1.0
Requires:	php-phpunit-PHP_Timer >= 1.0.4
Requires:	php-phpunit-Version >= 1.0.0
Requires:	php-symfony2-Console >= 2.7.7
Obsoletes:	php-phpunit-phpcpd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear Symfony/Component/.*

%description
Copy/Paste Detector (CPD) for PHP code.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install
install -p ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/phpcpd/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%attr(755,root,root) %{_bindir}/phpcpd
%{php_pear_dir}/SebastianBergmann/PHPCPD
