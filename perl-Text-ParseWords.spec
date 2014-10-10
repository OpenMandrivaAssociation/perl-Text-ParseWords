%define upstream_name    Text-ParseWords
%define upstream_version 3.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Parse strings containing shell-style quoting
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/Text-ParseWords-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildArch:	noarch

%description
The &nested_quotewords() and &quotewords() functions accept a delimiter
(which can be a regular expression) and a list of lines and then breaks
those lines up into a list of words ignoring delimiters that appear inside
quotes. &quotewords() returns all of the tokens in a single long list,
while &nested_quotewords() returns a list of token lists corresponding to
the elements of @lines. &parse_line() does tokenizing on a single string.
The &*quotewords() functions simply call &parse_line(), so if you're only
splitting one line you can call &parse_line() directly and save a function
call.

The $keep argument is a boolean flag. If true, then the tokens are split on
the specified delimiter, but all other characters (quotes, backslashes,
etc.) are kept in the tokens. If $keep is false then the &*quotewords()
functions remove all quotes and backslashes that are not themselves
backslash-escaped or inside of single quotes (i.e., &quotewords() tries to
interpret these characters just like the Bourne shell). NB: these semantics
are significantly different from the original version of this module
shipped with Perl 5.000 through 5.004. As an additional feature, $keep may
be the keyword "delimiters" which causes the functions to preserve the
delimiters in each string as tokens in the token lists, in addition to
preserving quote and backslash characters.

&shellwords() is written as a special case of &quotewords(), and it does
token parsing with whitespace as a delimiter-- similar to most Unix shells.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 3.270.0-3mdv2011.0
+ Revision: 658552
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.270.0-2mdv2011.0
+ Revision: 552180
- rebuild

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 3.270.0-1mdv2010.0
+ Revision: 395250
- import perl-Text-ParseWords


* Sun Jul 12 2009 cpan2dist 3.27-1mdv
- initial mdv release, generated with cpan2dist

